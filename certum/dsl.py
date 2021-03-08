from typing import Any, List

from certum.decipher import args_to_rule_decipher
from certum.exception import CertumException
from certum.rule.generic.abstract import DictRule
from certum.rule.generic.foreach import DictRuleForeach
from certum.rule.generic.forsome import DictRuleForsome
from certum.rule.shared.equals import DictRuleEqual
from certum.rule.shared.has_length_of import DictRuleLength
from certum.rule.shared.has_unique_elements import DictRuleUniqueElements
from certum.rule.shared.is_empty import DictRuleEmpty
from certum.rule.shared.is_instance_of import DictRuleInstanceOf
from certum.rule.shared.is_not_empty import DictRuleNotEmpty


class DictRuleDsl:
    """
    Entry point of the dsl
    """

    def __init__(self, path: List[str]) -> None:
        """Constructor method"""
        self.path = path

    def exists(self) -> DictRule:
        """Check if the current path exists.

        :return: The DictRule related with this rule.
        :rtype: DictRule
        """
        return DictRule(self.path)

    def forsome(self, *args, **kwargs) -> DictRuleForsome:
        """Check if the current path respect a list of rules for elements corresponding
        to some keys.

        .. note::

            Forsome needs a parameter 'keys' that contains the keys to analyse.

        :return: The DictRule related with this rule.
        :rtype: DictRuleForsome
        """
        try:
            keys = kwargs["keys"]
            if not isinstance(keys, list):
                raise CertumException("Forsome needs a 'keys' argument of type list")
        except KeyError as error:
            raise CertumException(
                "Forsome needs a 'keys' argument of type list"
            ) from error
        rules = args_to_rule_decipher(*args)
        return DictRuleForsome(self.path, keys, rules)

    def foreach(self, *args) -> DictRuleForeach:
        """Check if the current path respect a list of rules for each elements.

        :return: The DictRule related with this rule.
        :rtype: DictRuleForeach
        """
        rules = args_to_rule_decipher(*args)
        return DictRuleForeach(self.path, rules)

    def is_empty(self) -> DictRuleEmpty:
        """Check if the current path is empty.

        :return: The DictRule related with this rule.
        :rtype: DictRuleEmpty
        """
        return DictRuleEmpty(self.path)

    def is_not_empty(self) -> DictRuleNotEmpty:
        """Check if the current path is not empty.

        :return: The DictRule related with this rule.
        :rtype: DictRuleNotEmpty
        """
        return DictRuleNotEmpty(self.path)

    def is_instance_of(self, type_: type) -> DictRuleNotEmpty:
        """Check if the current path is instance of a type type_.

        :return: The DictRule related with this rule.
        :rtype: DictRuleNotEmpty
        """
        return DictRuleInstanceOf(self.path, type_)

    def has_length_of(self, length: int) -> DictRuleLength:
        """Check if the current path has a specific length.

        .. info:: For non iterable element, the length is 1.

        :return: The DictRule related with this rule.
        :rtype: DictRuleLength
        """
        return DictRuleLength(self.path, length)

    def has_unique_elements(self) -> DictRuleUniqueElements:
        """Check if the current path has unique elements.

        .. info:: For non iterable element, this is always True.

        :return: The DictRule related with this rule.
        :rtype: DictRuleUniqueElements
        """
        return DictRuleUniqueElements(self.path)

    def equals(self, value: Any) -> DictRuleEqual:
        """Check if the current path equals a value.

        :return: The DictRule related with this rule.
        :rtype: DictRuleEqual
        """
        return DictRuleEqual(self.path, value)
