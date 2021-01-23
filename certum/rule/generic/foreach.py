from typing import Any, Dict, List

from certum.rule.generic.abstract import JsonRule


class JsonRuleForeach(JsonRule):
    """The rule ensuring that a list of rules is respected for each elements
    of a dict or a list.

    :param path: The path where the keys should be presents.
    :type path: str
    :param keys: The keys itselves.
    :type keys: List[str]
    """

    def __init__(self, path: str, rules: List[JsonRule]):
        """Constructor method"""
        self.path = path
        self.rules = rules

    def check(self, json: Dict[str, Any]):
        target = self.target(json)
        values = target if isinstance(target, list) else target.keys()
        for rule in self.rules.copy():
            rule_path = rule.path
            for index, child in enumerate(values):
                key = index if isinstance(target, list) else child
                if rule_path:
                    rule.path = f"{self.path} -> {key} -> {rule_path}"
                else:
                    rule.path = f"{self.path} -> {key}"
                rule.check(json)
