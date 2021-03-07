from typing import Any, List

from certum.decipher import args_to_rule_decipher
from certum.rule.dict.contains_key import DictRuleKeyPresent
from certum.rule.dict.contains_keys import DictRuleKeysPresent
from certum.rule.dict.has_key_type import DictRuleKeyType
from certum.rule.dict.has_key_value import DictRuleKeyEqual
from certum.rule.dict.is_dict import DictRuleDict
from certum.rule.generic.abstract import DictRule
from certum.rule.generic.foreach import DictRuleForeach
from certum.rule.list.is_list import DictRuleList
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

    def foreach(self, *args) -> DictRuleForeach:
        """Check if the current path respect a list of rules for each elements.

        :return: The DictRule related with this rule.
        :rtype: DictRuleForeach
        """
        rules = args_to_rule_decipher(*args)
        return DictRuleForeach(self.path, rules)

    def is_list(self) -> DictRuleList:
        """Check if the current path is a list.

        :return: The DictRule related with this rule.
        :rtype: DictRuleList
        """
        return DictRuleList(self.path)

    def is_dict(self) -> DictRuleDict:
        """Check if the current path is a dict.

        :return: The DictRule related with this rule.
        :rtype: DictRuleDict
        """
        return DictRuleDict(self.path)

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

    def has_key_value(self, key: str, value: Any) -> DictRuleKeyEqual:
        """Check if the current path contains the provided key/value pair.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.DictRuleDict`
            - :class:`certum.rule.dict.contains_key.DictRuleKeyPresent`

        :return: The DictRule related with this rule.
        :rtype: DictRuleKeyEqual
        """
        return DictRuleKeyEqual(self.path, key, value)

    def has_key_type(self, key: str, value: Any) -> DictRuleKeyType:
        """Check if the current path contains a key with a specific type.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.DictRuleDict`
            - :class:`certum.rule.dict.contains_key.DictRuleKeyPresent`

        :return: The DictRule related with this rule.
        :rtype: DictRuleKeyType
        """
        return DictRuleKeyType(self.path, key, value)

    def equals(self, value: Any) -> DictRuleEqual:
        """Check if the current path equals a value.

        :return: The DictRule related with this rule.
        :rtype: DictRuleEqual
        """
        return DictRuleEqual(self.path, value)

    def contains_key(self, key: str) -> DictRuleKeyPresent:
        """Check if the current path contains a key.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.DictRuleDict`

        :return: The DictRule related with this rule.
        :rtype: DictRuleKeyPresent
        """
        return DictRuleKeyPresent(self.path, key)

    def contains_keys(self, keys: List[str]) -> DictRuleKeysPresent:
        """Check if the current path contains a list of keys.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.DictRuleDict`

        :return: The DictRule related with this rule.
        :rtype: DictRuleKeysPresent
        """
        return DictRuleKeysPresent(self.path, keys)
