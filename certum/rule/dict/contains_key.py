from typing import Any, Dict

from certum.rule.dict.is_dict import JsonRuleDict
from certum.rule.generic.abstract import JsonRule


class JsonRuleKeyPresent(JsonRule):
    """The rule ensuring that a key is present inside a path.

    :param path: The path where the key should be present.
    :type path: str
    :param key: The key itself.
    :type key: str
    """

    def __init__(self, path: str, key: str):
        """Constructor method"""
        self.path = path
        self.key = key

    def check(self, json: Dict[str, Any]):
        """Check if the path from the corresponding json is a dict containing
        the key 'self.key'.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.JsonRuleDict`

        :raises AssertionError: if the path's dict doesn't contain the key.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        """
        JsonRuleDict(self.path).check(json)
        message = f"The key {self.key} is missing."
        assert self.key in self.target(json), self.error(message)
