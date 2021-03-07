from typing import Any, Dict, List

from certum.error import Error
from certum.exception import CertumException
from certum.private import _target


class DictRule:
    """The base for all rules.

    It provides the error system and the target function.

    :param path: The path targeted by the rule.
    :type path: List[str]
    """

    def __init__(self, path: List[str]):
        """Constructor method"""
        self.path = path

    def target(self, dictionary: Dict[str, Any]) -> Any:
        """Target a value following the path 'self.path' inside the dictionary.

        :Example:

        path = ["a", 0, "b"]
        obj = {"a": [{"b": 1}]}
        assert DictRule(path).target(obj) == 1 # True

        :param dictionary: The targeting dictionary.
        :type dictionary: Dict[str, Any]
        :raises (TypeError, ValueError, KeyError): if the path doesn't exist.
        :return: The value of the path.
        :rtype: Any
        """
        return _target(self.path, dictionary)

    def error(self, message: str) -> Error:
        """Format error message throws by the assertion.

        :param message: The cause of the error.
        :type message: str
        :return: The formatted message.
        :rtype: str
        """
        return Error(self.path, message)

    def check(self, dictionary: Dict[str, Any]) -> List[Error]:
        """Check if the rule is respected.

        :raises AssertionError: if the rule is not respected.
        :param dictionary: [description]
        :type dictionary: Dict[str, Any]
        """
        for index, key in enumerate(self.path, 1):
            try:
                _target(self.path[:index], dictionary)
            except CertumException:
                error = Error(self.path[:index], "The path is missing.")
                return [error]
        return []
