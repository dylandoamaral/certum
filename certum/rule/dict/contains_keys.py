from typing import Any, Dict, List

from certum.error import Error
from certum.rule.dict.contains_key import JsonRuleKeyPresent
from certum.rule.dict.is_dict import JsonRuleDict
from certum.rule.generic.abstract import JsonRule


class JsonRuleKeysPresent(JsonRule):
    """The rule ensuring that keys are presents inside a path.

    :param path: The path where the keys should be presents.
    :type path: str
    :param keys: The keys itselves.
    :type keys: List[str]
    """

    def __init__(self, path: str, keys: List[str]):
        """Constructor method"""
        self.path = path
        self.keys = keys

    def check(self, json: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding json is a dict containing
        the keys inside 'self.keys'.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.JsonRuleDict`
            - :class:`certum.rule.dict.contains_key.JsonRuleKeyPresent`

        :raises AssertionError: if the path's dict doesn't contain the keys.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = JsonRuleDict(self.path).check(json)
        for key in self.keys:
            errors += JsonRuleKeyPresent(self.path, key).check(json)
        return errors
