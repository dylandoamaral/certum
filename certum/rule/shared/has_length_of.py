from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import DictRule


class DictRuleLength(DictRule):
    """The rule ensuring that a path has a particular length.

    :param path: The path where the key should be present.
    :type path: List[Any]
    :param value: The length of the this of the path.
    :type value: int
    """

    def __init__(self, path: List[Any], length: int):
        """Constructor method"""
        self.path = path
        self.length = length

    def check(self, dictionary: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding has a particular length.

        :raises AssertionError: if the path doesn't have a particular length.
        :param dictionary: The Dict to analyse.
        :type dictionary: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = super().check(dictionary)
        if errors:
            return errors
        try:
            _length = len(self.target(dictionary))
        except TypeError:
            # TODO Probably add verification in case of value who is not
            # elligible with len function and return an assertion error.
            _length = 1
        path = " -> ".join(self.path)
        message = f"The length of {path} is {_length}" f", expected {self.length}."
        if _length != self.length:
            errors.append(self.error(message))
        return errors
