from typing import Any, Dict, List

from certum.error import Error
from certum.rule.dict.contains_key import JsonRuleKeyPresent
from certum.rule.dict.is_dict import JsonRuleDict
from certum.rule.generic.abstract import JsonRule


class JsonRuleKeyEqual(JsonRule):
    """The rule ensuring that a key inside a path has a particular value.

    :param path: The path where the key should be present.
    :type path: List[str]
    :param key: The key itself.
    :type key: str
    :param value: The value of the key.
    :type value: Any
    """

    def __init__(self, path: List[str], key: str, value: Any):
        """Constructor method"""
        self.path = path
        self.key = key
        self.value = value

    def check(self, json: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding json is a dict containing
        the key 'self.key' of value 'self.value'.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.JsonRuleDict`
            - :class:`certum.rule.dict.contains_key.JsonRuleKeyPresent`

        :raises AssertionError: if the path's dict contains the key with an
                                incorrect value.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = JsonRuleDict(self.path).check(json)
        errors += JsonRuleKeyPresent(self.path, self.key).check(json)
        _value = self.target(json)[self.key]
        message = f"The key {self.key} is not equal to {self.value} but {_value}."
        if _value != self.value:
            errors.append(self.error(message))
        return errors
