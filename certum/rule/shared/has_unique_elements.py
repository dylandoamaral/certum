from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import JsonRule


class JsonRuleUniqueElements(JsonRule):
    """The rule ensuring that a path has only unique elements.

    :param path: The path where the key should be present.
    :type path: List[str]
    """

    def __init__(self, path: List[str]):
        """Constructor method"""
        self.path = path

    def check(self, json: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding json has unique elements.

        :raises AssertionError: if the path doesn't have unique elements.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        target = self.target(json)
        try:
            _length = len(target)
        except TypeError:
            # TODO Probably add verification in case of value who is not an
            # list or a dict.
            return []

        errors = []

        for i in range(0, _length - 1):
            for j in range(1, _length):
                if i != j:
                    if isinstance(target, dict):
                        keys = list(target.keys())
                        first = target[keys[i]]
                        second = target[keys[j]]
                    else:
                        first = target[i]
                        second = target[j]
                    message = f"The row {i} and {j} are the same."
                    if first == second:
                        errors.append(self.error(message))
        return errors
