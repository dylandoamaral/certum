from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import JsonRule


class JsonRuleInstanceOf(JsonRule):
    """The rule ensuring that a path is instance of a type type_.

    :param path: The path that should be of type type_.
    :type path: List[str]
    :param type_: The expected type.
    :type type_: type
    """

    def __init__(self, path: List[str], type_: type):
        """Constructor method"""
        self.path = path
        self.type_ = type_

    def check(self, json: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding json is instance of a type.

        :raises AssertionError: if the path isn't instance of the type type_.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        value = self.target(json)
        path = " -> ".join(self.path)
        real_type = type(value)
        message = (
            f"The path {path} is not instance of {self.type_.__name__} "
            f"but {real_type.__name__}."
        )
        if real_type != self.type_:
            return [self.error(message)]
        return []
