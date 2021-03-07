from typing import Any, Dict, List

from certum.error import Error
from certum.rule.dict.is_dict import DictRuleDict
from certum.rule.generic.abstract import DictRule


class DictRuleKeyPresent(DictRuleDict):
    """The rule ensuring that a key is present inside a path.

    :param path: The path where the key should be present.
    :type path: List[str]
    :param key: The key itself.
    :type key: str
    """

    def __init__(self, path: List[str], key: str):
        """Constructor method"""
        self.path = path
        self.key = key

    def check(self, dictionary: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding dictionary is a dict containing
        the key 'self.key'.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.DictRuleDict`

        :raises AssertionError: if the path's dict doesn't contain the key.
        :param dictionary: The Dict to analyse.
        :type dictionary: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = super().check(dictionary)
        if errors:
            return errors
        message = f"The key {self.key} is missing."
        if self.key not in self.target(dictionary):
            errors.append(self.error(message))
        return errors
