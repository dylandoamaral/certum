from dataclasses import dataclass, field
from typing import Any, Dict, List

from certum.decipher import args_to_rule_decipher
from certum.exception import CertumException
from certum.rule.generic.abstract import JsonRule
from certum.strategy.abstract import Strategy
from certum.strategy.filtering.abstract import FilteringStrategy
from certum.strategy.filtering.no import NoFiltering
from certum.strategy.printing.abstract import PrintingStrategy
from certum.strategy.printing.simple import SimplePrinting
from certum.strategy.sorting.abstract import SortingStrategy
from certum.strategy.sorting.no import NoSorting


@dataclass
class JsonValidator:
    """The class that wrap the json to analyse and provide function to check
    it based on :class:`certum.rule.generic.abstract.JsonRule`.

    .. warning:: You should always use `certum.that` to create a validator.

    :param path: The path where the key should be present.
    :type path: List[str]
    :param key: The key itself.
    :type key: str
    :param sorting: The sorting strategy to use.
    :type sorting: SortingStrategy
    :param filtering: The filtering strategy to use.
    :type filtering: FilteringStrategy
    :param printing: The printing strategy to use.
    :type printing: PrintingStrategy
    """

    json: Dict[str, Any]
    rules: List[JsonRule] = field(default_factory=list)
    sorting: SortingStrategy = NoSorting()
    filtering: FilteringStrategy = NoFiltering()
    printing: PrintingStrategy = SimplePrinting()

    def respects(self, *args) -> "JsonValidator":
        """Provide a bunch of rules that need to be respected by the self.json
        dictionary. These rules can be provided using
        :class:`certum.rule.generic.abstract.JsonRule` or lists of
        :class:`certum.rule.generic.abstract.JsonRule`.

        :raises CertumException: if one argument is not a JsonRule complient
                                 argument.
        :return: Itself.
        :rtype: JsonValidator
        """
        rules = args_to_rule_decipher(*args)
        return JsonValidator(
            self.json, self.rules + rules, self.sorting, self.filtering, self.printing
        )

    def using(self, *args) -> "JsonValidator":
        """Setup strategies to use by the validator. These strategies can be provided
        using :class:`certum.strategy.abstract.Strategy` or lists of
        :class:`certum.strategy.abstract.Strategy`.

        :raises CertumException: If the argument provided is not a available strategy.
        :return: Itself.
        :rtype: JsonValidator
        """

        def setup_strategy(validator, strategy) -> "JsonValidator":
            if isinstance(strategy, SortingStrategy):
                validator.sorting = strategy
            elif isinstance(strategy, FilteringStrategy):
                validator.filtering = strategy
            elif isinstance(strategy, PrintingStrategy):
                validator.printing = strategy
            else:
                raise CertumException(
                    "The strategy provided for the validator is uknown."
                )
            return validator

        for arg in args:
            if isinstance(arg, list):
                for strategy in arg:
                    setup_strategy(self, strategy)
            elif isinstance(arg, Strategy):
                setup_strategy(self, arg)
            else:
                raise CertumException(
                    "The strategy provided for the validator is uknown."
                )

        return self

    def check(self):
        """Check all provided rules and throw an error if at least one of them
        is not respected.

        :param sorting: The sorting strategy used to sort errors, defaults to
                        NoSorting()
        :type sorting: SortingStrategy, optional
        :param filtering: The sorting strategy used to sort errors, defaults to
                        NoSorting()
        :type filtering: FilteringStrategy, optional
        :param printing: The filtering strategy used to filter errors, defaults to
                         NoFiltering()
        :type printing: FilteringStrategy, optional
        :raises CertumException: if at least one rule is not respected.
        """
        errors = [err for rule in self.rules for err in rule.check(self.json)]
        errors = self.sorting.sort(errors)
        errors = self.filtering.filter(errors)
        if errors:
            raise CertumException(f"\n\n{self.printing.print(errors)}")
