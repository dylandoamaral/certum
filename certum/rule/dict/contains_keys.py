from typing import Any, Dict, List

from certum.error import Error
from certum.rule.dict.contains_key import DictRuleKeyPresent
from certum.rule.dict.is_dict import DictRuleDict
from certum.rule.generic.abstract import DictRule


class DictRuleKeysPresent(DictRuleDict):
    """The rule ensuring that keys are presents inside a path.

    :param path: The path where the keys should be presents.
    :type path: List[str]
    :param keys: The keys itselves.
    :type keys: List[str]
    """

    def __init__(self, path: List[str], keys: List[str]):
        """Constructor method"""
        self.path = path
        self.keys = keys

    def check(self, dictionary: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding dictionary is a dict containing
        the keys inside 'self.keys'.

        Embedded rules:
            - :class:`certum.rule.dict.is_dict.DictRuleDict`
            - :class:`certum.rule.dict.contains_key.DictRuleKeyPresent`

        :raises AssertionError: if the path's dict doesn't contain the keys.
        :param dictionary: The Dict to analyse.
        :type dictionary: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = super().check(dictionary)
        if errors:
            return errors
        for key in self.keys:
            errors += DictRuleKeyPresent(self.path, key).check(dictionary)
        return errors
