from typing import Any, List

from certum.decipher import args_to_rule_decipher
from certum.rule.list.is_list import JsonRulelist
from certum.rule.dict.contains_key import JsonRuleKeyPresent
from certum.rule.dict.contains_keys import JsonRuleKeysPresent
from certum.rule.dict.has_key_type import JsonRuleKeyType
from certum.rule.dict.has_key_value import JsonRuleKeyEqual
from certum.rule.dict.is_dict import JsonRuleDict
from certum.rule.generic.foreach import JsonRuleForeach
from certum.rule.shared.equals import JsonRuleEqual
from certum.rule.shared.has_length_of import JsonRuleLength
from certum.rule.shared.has_unique_elements import JsonRuleUniquethis
from certum.rule.shared.is_empty import JsonRuleEmpty
from certum.rule.shared.is_not_empty import JsonRuleKeyNotEmpty


class JsonRuleDsl:
    """
    Entry point of the dsl
    """

    def __init__(self, path: str) -> None:
        """Constructor method"""
        self.path = path

    def foreach(self, *args) -> JsonRuleForeach:
        rules = args_to_rule_decipher(*args)
        return JsonRuleForeach(self.path, rules)

    def is_list(self) -> JsonRulelist:
        """Check if the current path is a list.

        :return: The JsonRule related with this rule.
        :rtype: JsonRulelist
        """
        return JsonRulelist(self.path)

    def is_dict(self) -> JsonRuleDict:
        return JsonRuleDict(self.path)

    def is_empty(self) -> JsonRuleEmpty:
        return JsonRuleEmpty(self.path)

    def is_not_empty(self) -> JsonRuleKeyNotEmpty:
        return JsonRuleKeyNotEmpty(self.path)

    def has_length_of(self, length: int) -> JsonRuleLength:
        return JsonRuleLength(self.path, length)

    def has_unique_elements(self) -> JsonRuleUniquethis:
        return JsonRuleUniquethis(self.path)

    def has_key_value(self, key: str, value: Any) -> JsonRuleKeyEqual:
        return JsonRuleKeyEqual(self.path, key, value)

    def has_key_type(self, key: str, value: Any) -> JsonRuleKeyType:
        return JsonRuleKeyType(self.path, key, value)

    def equals(self, value: Any) -> JsonRuleEqual:
        return JsonRuleEqual(self.path, value)

    def contains_key(self, key: str) -> JsonRuleKeyPresent:
        return JsonRuleKeyPresent(self.path, key)

    def contains_keys(self, keys: List[str]) -> JsonRuleKeysPresent:
        return JsonRuleKeysPresent(self.path, keys)
