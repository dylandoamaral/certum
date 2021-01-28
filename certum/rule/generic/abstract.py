from abc import ABC, abstractmethod
from typing import Any, Dict, List

from certum.error import Error
from certum.exception import CertumException


class JsonRule(ABC):
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

        A path is composed by keys separated by ' -> '.

        :Example:

        path = "a -> 0 -> b"
        obj = {"a": [{"b": 1}]}
        assert JsonRule(path).target(obj) == 1 # True

        :param json: The targeting json.
        :type json: Dict[str, Any]
        :raises (TypeError, ValueError): if the path doesn't exist.
        :return: The value of the path.
        :rtype: Any
        """
        if not self.path:
            return json
        current = json
        for key in self.path:
            try:
                if isinstance(current, list):
                    current = current[int(key)]
                else:
                    current = current[key]
            except (TypeError, ValueError):
                path = " -> ".join(self.path)
                raise CertumException(f"The path {path} doesn't not exist")
        return current

    def error(self, message: str) -> Error:
        """Format error message throws by the assertion.

        :param message: The cause of the error.
        :type message: str
        :return: The formatted message.
        :rtype: str
        """
        return Error(self.path, message)

    @abstractmethod
    def check(self, json: Dict[str, Any]) -> List[Error]:
        """Check if the rule is respected.

        :raises AssertionError: if the rule is not respected.
        :param json: [description]
        :type json: Dict[str, Any]
        """
        pass
