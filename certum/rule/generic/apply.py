from typing import Any, Callable, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import DictRule


class DictRuleApply(DictRule):
    """The rule ensuring that a path apply a function without returning an error.

    :param path: The path where the key should be present.
    :type path: List[str]
    :param fn: The function from the target of the path to the error messages.
    :type fn: Callable[[Any], List[str]]
    """

    def __init__(self, path: List[str], fn: Callable[[Any], List[str]]):
        """Constructor method"""
        self.path = path
        self.fn = fn

    def check(self, dictionary: Dict[str, Any]) -> List[Error]:
        """Check if the path apply a function without returning an error.

        :raises AssertionError: if the path doesn't equal the value.
        :param dictionary: The Dict to analyse.
        :type dictionary: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = super().check(dictionary)
        if errors:
            return errors
        _value = self.target(dictionary)
        return [self.error(message) for message in self.fn(_value)]
