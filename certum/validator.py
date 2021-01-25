from typing import Any, Dict, List

from certum.decipher import args_to_rule_decipher
from certum.exception import CertumException
from certum.printing.abstract import PrintingStrategy
from certum.printing.simple import SimplePrinting
from certum.rule.generic.abstract import JsonRule
from certum.sorting.abstract import SortingStrategy
from certum.sorting.alphabetical import AlphabeticalSorting


class JsonValidator:
    """The class that wrap the json to analyse and provide function to check
    it based on :class:`certum.rule.generic.abstract.JsonRule`.

    .. warning:: You should always use `certum.that` to create a validator.

    :param path: The path where the key should be present.
    :type path: str
    :param key: The key itself.
    :type key: str
    """

    def __init__(self, json: Dict[str, Any], rules: List[JsonRule] = None):
        """Constructor method"""
        self.json = json
        self.rules = rules or []

    def respects(self, *args) -> List[JsonRule]:
        """Provide a bunch of rules that need to be respected by the self.json
        dictionary. These rules can be provided using
        :class:`certum.rule.generic.abstract.JsonRule` or lists of
        :class:`certum.rule.generic.abstract.JsonRule`.

        :raises CertumException: if one argument is not a JsonRule complient
                                 argument.
        :return: A list of :class:`certum.rule.generic.abstract.JsonRule`.
        :rtype: List[JsonRule]
        """
        rules = args_to_rule_decipher(*args)
        for rule in rules:
            self.rules.append(rule)
        return self

    def check(
        self,
        sorting: SortingStrategy = AlphabeticalSorting(),
        printing: PrintingStrategy = SimplePrinting(),
    ):
        """Check all provided rules and throw an error if at least one of them
        is not respected.

        :param sorting: The sorting strategy used to sort errors, defaults to
                        AlphabeticalSorting()
        :type sorting: SortingStrategy, optional
        :param printing: The printing strategy used to print errors, defaults to
                         SimplePrinting()
        :type printing: PrintingStrategy, optional
        :raises CertumException: if at least one rule is not respected.
        """
        errors = [err for rule in self.rules for err in rule.check(self.json)]
        errors = sorting.sort(errors)
        if errors:
            raise CertumException(f"\n\n{printing.print(errors)}")
