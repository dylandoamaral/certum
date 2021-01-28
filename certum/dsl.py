from typing import Any, List

from certum.decipher import args_to_rule_decipher
from certum.rule.dict.contains_key import JsonRuleKeyPresent
from certum.rule.dict.contains_keys import JsonRuleKeysPresent
from certum.rule.dict.has_key_type import JsonRuleKeyType
from certum.rule.dict.has_key_value import JsonRuleKeyEqual
from certum.rule.dict.is_dict import JsonRuleDict
from certum.rule.generic.foreach import JsonRuleForeach
from certum.rule.list.is_list import JsonRuleList
from certum.rule.shared.equals import JsonRuleEqual
from certum.rule.shared.has_length_of import JsonRuleLength
from certum.rule.shared.has_unique_elements import JsonRuleUniqueElements
from certum.rule.shared.is_empty import JsonRuleEmpty
from certum.rule.shared.is_not_empty import JsonRuleKeyNotEmpty


class JsonRuleDsl:
    """
    Entry point of the dsl
    """

    def __init__(self, path: List[str]) -> None:
        """Constructor method"""
        self.path = path

    def foreach(self, *args) -> JsonRuleForeach:
        """Check if the current path respect a list of rules for each elements.

        :return: The JsonRule related with this rule.
        :rtype: JsonRuleForeach
        """
        rules = args_to_rule_decipher(*args)
        return JsonRuleForeach(self.path, rules)

    def is_list(self) -> JsonRuleList:
        """Check if the current path is a list.

        :return: The JsonRule related with this rule.
        :rtype: JsonRuleList
        """
        return JsonRuleList(self.path)

    def is_dict(self) -> JsonRuleDict:
        """Check if the current path is a dict.

        :return: The JsonRule related with this rule.
        :rtype: JsonRuleDict
        """
        return JsonRuleDict(self.path)

    def is_empty(self) -> JsonRuleEmpty:
        """Check if the current path is empty.

        :return: The JsonRule related with this rule.
        :rtype: JsonRuleEmpty
        """
        return JsonRuleEmpty(self.path)

    def is_not_empty(self) -> JsonRuleKeyNotEmpty:
        """Check if the current path is not empty.

        :return: The JsonRule related with this rule.
        :rtype: JsonRuleKeyNotEmpty
        """
        return JsonRuleKeyNotEmpty(self.path)

    def has_length_of(self, length: int) -> JsonRuleLength:
        """Check if the current path has a specific length.

        .. info:: For non iterable element, the length is 1.

        :return: The JsonRule related with this rule.
        :rtype: JsonRuleLength
        """
        return JsonRuleLength(self.path, length)

    def has_unique_elements(self) -> JsonRuleUniqueElements:
        """Check if the current path has unique elements.

        .. info:: For non iterable element, this is always True.

        :return: The JsonRule related with this rule.
        :rtype: JsonRuleUniqueElements
        """
        return JsonRuleUniqueElements(self.path)

    def has_key_value(self, key: str, value: Any) -> JsonRuleKeyEqual:
        """Check if the current path contains the provided key/value pair.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.JsonRuleDict`
            - :class:`certum.rule.dict.contains_key.JsonRuleKeyPresent`

        :return: The JsonRule related with this rule.
        :rtype: JsonRuleKeyEqual
        """
        return JsonRuleKeyEqual(self.path, key, value)

    def has_key_type(self, key: str, value: Any) -> JsonRuleKeyType:
        """Check if the current path contains a key with a specific type.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.JsonRuleDict`
            - :class:`certum.rule.dict.contains_key.JsonRuleKeyPresent`

        :return: The JsonRule related with this rule.
        :rtype: JsonRuleKeyType
        """
        return JsonRuleKeyType(self.path, key, value)

    def equals(self, value: Any) -> JsonRuleEqual:
        """Check if the current path equals a value.

        :return: The JsonRule related with this rule.
        :rtype: JsonRuleEqual
        """
        return JsonRuleEqual(self.path, value)

    def contains_key(self, key: str) -> JsonRuleKeyPresent:
        """Check if the current path contains a key.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.JsonRuleDict`

        :return: The JsonRule related with this rule.
        :rtype: JsonRuleKeyPresent
        """
        return JsonRuleKeyPresent(self.path, key)

    def contains_keys(self, keys: List[str]) -> JsonRuleKeysPresent:
        """Check if the current path contains a list of keys.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.JsonRuleDict`

        :return: The JsonRule related with this rule.
        :rtype: JsonRuleKeysPresent
        """
        return JsonRuleKeysPresent(self.path, keys)
