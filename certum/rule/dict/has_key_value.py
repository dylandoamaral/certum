from typing import Any, Dict, List

from certum.error import Error
from certum.rule.dict.contains_key import DictRuleKeyPresent
from certum.rule.dict.is_dict import DictRuleDict
from certum.rule.generic.abstract import DictRule


class DictRuleKeyEqual(DictRuleDict):
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

    def check(self, dictionary: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding dictionary is a dict containing
        the key 'self.key' of value 'self.value'.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.DictRuleDict`
            - :class:`certum.rule.dict.contains_key.DictRuleKeyPresent`

        :raises AssertionError: if the path's dict contains the key with an
                                incorrect value.
        :param dictionary: The Dict to analyse.
        :type dictionary: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = super().check(dictionary)
        if errors:
            return errors
        errors = DictRuleKeyPresent(self.path, self.key).check(dictionary)
        _value = self.target(dictionary)[self.key]
        message = f"The key {self.key} is not equal to {self.value} but {_value}."
        if _value != self.value:
            errors.append(self.error(message))
        return errors
