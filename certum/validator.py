from typing import Any, Dict, List

from certum.decipher import args_to_rule_decipher
from certum.rule.generic.abstract import JsonRule


class JsonValidator:
    """The class that wrap the json to analyse and provide function to check
    it based on :class:`certum.rule.generic.abstract.JsonRule`.

    .. warning:: You should always use `certum.that` to create a validator.

    :param path: The path where the key should be present.
    :type path: str
    :param key: The key itself.
    :type key: str
    """

    def __init__(self, json: Dict[str, Any], rules: List[JsonRule] = None):
        """Constructor method"""
        self.json = json
        self.rules = rules or []

    def respects(self, *args):
        """Provide a bunch of rules that need to be respected by the self.json
        dictionary. These rules can be provided using
        :class:`certum.rule.generic.abstract.JsonRule` or lists of
        :class:`certum.rule.generic.abstract.JsonRule`.

        :raises CertumException: if one argument is not a JsonRule complient
                                 argument.
        :return: [description]
        :rtype: [type]
        """
        rules = args_to_rule_decipher(*args)
        for rule in rules:
            self.rules.append(rule)
        return self

    def check(self):
        """Check all provided rules and throw an error if one of them is not
        respected.

        :raises AssertionError: if one rule is not respected.
        """
        for rule in self.rules:
            rule.check(self.json)
