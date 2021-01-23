from typing import Any, Dict, List

from certum.decipher import args_to_rule_decipher
from certum.rule.generic.abstract import JsonRule


class JsonValidator:
    def __init__(self, json: Dict[str, Any], rules: List[JsonRule] = None):
        """Constructor method"""
        self.json = json
        self.rules = rules or []

    def respects(self, *args):
        rules = args_to_rule_decipher(*args)
        for rule in rules:
            self.rules.append(rule)
        return self

    def check(self):
        for rule in self.rules:
            rule.check(self.json)
