from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from certum.decipher import args_to_rule_decipher
from certum.exception import CertumException
from certum.private import _using
from certum.rule.generic.abstract import DictRule
from certum.strategy.filtering.abstract import FilteringStrategy
from certum.strategy.filtering.no import NoFiltering
from certum.strategy.printing.abstract import PrintingStrategy
from certum.strategy.printing.simple import SimplePrinting
from certum.strategy.sorting.abstract import SortingStrategy
from certum.strategy.sorting.no import NoSorting


@dataclass
class DictValidator:
    """The class that wrap the dictionary to analyse and provide function to check
    it based on :class:`certum.rule.generic.abstract.DictRule`.

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

    dictionary: Optional[Dict[str, Any]] = None
    rules: List[DictRule] = field(default_factory=list)
    sorting: SortingStrategy = NoSorting()
    filtering: FilteringStrategy = NoFiltering()
    printing: PrintingStrategy = SimplePrinting()

    def respects(self, *args) -> "DictValidator":
        """Provide a bunch of rules that need to be respected by the self.dictionary
        dictionary. These rules can be provided using
        :class:`certum.rule.generic.abstract.DictRule` or lists of
        :class:`certum.rule.generic.abstract.DictRule`.

        :raises CertumException: if one argument is not a DictRule complient
                                 argument.
        :return: Itself.
        :rtype: DictValidator
        """
        rules = args_to_rule_decipher(*args)
        return DictValidator(
            self.dictionary,
            self.rules + rules,
            self.sorting,
            self.filtering,
            self.printing,
        )

    def using(self, *args) -> "DictValidator":
        """Setup strategies to use by the validator. These strategies can be provided
        using :class:`certum.strategy.abstract.Strategy` or lists of
        :class:`certum.strategy.abstract.Strategy`.

        :raises CertumException: If the argument provided is not a available strategy.
        :return: Itself.
        :rtype: DictValidator
        """
        return _using(*args, validator=self)

    def on(  # pylint: disable=C0103
        self, dictionary: Dict[str, Any]
    ) -> "DictValidator":
        """Attribute a new dictionary to analyse by the validator.

        :param dictionary: The dictionary to analyse.
        :type dictionary: Dict[str, Any]
        :return: Itself.
        :rtype: DictValidator
        """
        if not isinstance(dictionary, dict):
            raise CertumException("DictValidator need a dictionary of type dict.")
        return DictValidator(
            dictionary, self.rules, self.sorting, self.filtering, self.printing
        )

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
        errors = [err for rule in self.rules for err in rule.check(self.dictionary)]
        errors = list(set(errors))
        errors = self.sorting.sort(errors)
        errors = self.filtering.filter(errors)
        if errors:
            raise CertumException(f"\n\n{self.printing.print(errors)}")
