from typing import Any, Dict, List

from certum.error import Error
from certum.exception import CertumException
from certum.private import _target


class JsonRule:
    """The base for all rules.

    It provides the error system and the target function.

    :param path: The path targeted by the rule.
    :type path: List[str]
    """

    def __init__(self, path: List[str]):
        """Constructor method"""
        self.path = path

    def target(self, json: Dict[str, Any]) -> Any:
        """Target a value following the path 'self.path' inside the json.

        :Example:

        path = ["a", 0, "b"]
        obj = {"a": [{"b": 1}]}
        assert JsonRule(path).target(obj) == 1 # True

        :param json: The targeting json.
        :type json: Dict[str, Any]
        :raises (TypeError, ValueError, KeyError): if the path doesn't exist.
        :return: The value of the path.
        :rtype: Any
        """
        return _target(self.path, json)

    def error(self, message: str) -> Error:
        """Format error message throws by the assertion.

        :param message: The cause of the error.
        :type message: str
        :return: The formatted message.
        :rtype: str
        """
        return Error(self.path, message)

    def check(self, json: Dict[str, Any]) -> List[Error]:
        """Check if the rule is respected.

        :raises AssertionError: if the rule is not respected.
        :param json: [description]
        :type json: Dict[str, Any]
        """
        for index, key in enumerate(self.path, 1):
            try:
                _target(self.path[:index], json)
            except CertumException:
                error = Error(self.path[:index], "The path is missing.")
                return [error]
        return []
