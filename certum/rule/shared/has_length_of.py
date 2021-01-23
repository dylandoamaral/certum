from typing import Any, Dict

from certum.rule.generic.abstract import JsonRule


class JsonRuleLength(JsonRule):
    """The rule ensuring that a path has a particular length.

    :param path: The path where the key should be present.
    :type path: str
    :param value: The length of the this of the path.
    :type value: int
    """

    def __init__(self, path: str, length: int):
        """Constructor method"""
        self.path = path
        self.length = length

    def check(self, json: Dict[str, Any]):
        """Check if the path from the corresponding has a particular length.

        :raises AssertionError: if the path doesn't have a particular length.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        """
        try:
            _length = len(self.target(json))
        except TypeError:
            # TODO Probably add verification in case of value who is not
            # elligible with len function and return an assertion error.
            _length = 1

        message = f"The length of {self.path} is {_length}" f", expected {self.length}."
        assert _length == self.length, self.error(message)
