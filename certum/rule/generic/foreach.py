from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import JsonRule


class JsonRuleForeach(JsonRule):
    """The rule ensuring that a list of rules is respected for each elements
    of a dict or a list.

    :param path: The path where the keys should be presents.
    :type path: List[str]
    :param rules: The rules that should be applied.
    :type keys: List[JsonRule]
    """

    def __init__(self, path: List[str], rules: List[JsonRule]):
        """Constructor method"""
        self.path = path
        self.rules = rules

    def check(self, json: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding json respect a list of
        rules for each of his children.

        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        target = self.target(json)
        values = target if isinstance(target, list) else target.keys()
        errors = []
        for rule in self.rules.copy():
            rule_path = rule.path
            for index, child in enumerate(values):
                key = str(index) if isinstance(target, list) else child
                if rule_path != [""]:
                    rule.path = self.path + [key] + rule_path
                else:
                    rule.path = self.path + [key]
                errors += rule.check(json)
        return errors
