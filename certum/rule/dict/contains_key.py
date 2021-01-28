from typing import Any, Dict, List

from certum.error import Error
from certum.rule.dict.is_dict import JsonRuleDict
from certum.rule.generic.abstract import JsonRule


class JsonRuleKeyPresent(JsonRule):
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

    def check(self, json: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding json is a dict containing
        the key 'self.key'.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.JsonRuleDict`

        :raises AssertionError: if the path's dict doesn't contain the key.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = JsonRuleDict(self.path).check(json)
        message = f"The key {self.key} is missing."
        if self.key not in self.target(json):
            errors.append(self.error(message))
        return errors
