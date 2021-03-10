from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import DictRule
from certum.rule.generic.forsome import DictRuleForsome


class DictRuleForeach(DictRule):
    """The rule ensuring that a list of rules is respected for each elements
    of a dict or a list.

    :param path: The path where the keys should be presents.
    :type path: List[Any]
    :param rules: The rules that should be applied.
    :type keys: List[DictRule]
    """

    def __init__(self, path: List[Any], rules: List[DictRule]):
        """Constructor method"""
        self.path = path
        self.rules = rules

    def check(self, dictionary: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding dictionary respect a list of
        rules for each of his children.

        :param dictionary: The Dict to analyse.
        :type dictionary: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                no errors.
        :rtype: List[Error]
        """
        errors = super().check(dictionary)
        if errors:
            return errors
        target = self.target(dictionary)
        if not isinstance(target, dict) and not isinstance(target, list):
            errors += [self.error("The path should be instance of dict or list.")]
            return errors
        keys = range(0, len(target)) if isinstance(target, list) else target.keys()
        return DictRuleForsome(self.path, keys, self.rules).check(dictionary)
