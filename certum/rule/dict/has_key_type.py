from typing import Any, Dict

from certum.rule.dict.contains_key import JsonRuleKeyPresent
from certum.rule.dict.is_dict import JsonRuleDict
from certum.rule.generic.abstract import JsonRule


class JsonRuleKeyType(JsonRule):
    """The rule ensuring that a key inside a path has a particular type.

    :param path: The path where the key should be present.
    :type path: str
    :param key: The key itself.
    :type key: str
    :param value: The type of the key.
    :type value: Any
    """

    def __init__(self, path: str, key: str, value: Any):
        """Constructor method"""
        self.path = path
        self.key = key
        self.value = value

    def check(self, json: Dict[str, Any]):
        """Check if the path from the corresponding json is a dict containing
        the key 'self.key' of type 'self.value'.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.JsonRuleDict`
            - :class:`certum.rule.dict.contains_key.JsonRuleKeyPresent`

        :raises AssertionError: if the path's dict contains the key with an
                                incorrect type.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        """
        JsonRuleDict(self.path).check(json)
        JsonRuleKeyPresent(self.path, self.key).check(json)
        _value = self.target(json)[self.key]
        message = (
            f"The key {self.key} is not an instance of "
            f"{self.value.__name__} but {type(_value).__name__}."
        )
        assert isinstance(_value, self.value), self.error(message)
