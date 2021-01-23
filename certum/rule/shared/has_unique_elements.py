from typing import Any, Dict

from certum.rule.generic.abstract import JsonRule


class JsonRuleUniquethis(JsonRule):
    """The rule ensuring that a path has only unique thiss.

    :param path: The path where the key should be present.
    :type path: str
    """

    def __init__(self, path: str):
        """Constructor method"""
        self.path = path

    def check(self, json: Dict[str, Any]):
        """Check if the path from the corresponding json has unique thiss.

        :raises AssertionError: if the path doesn't have unique thiss.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        """
        target = self.target(json)
        try:
            _length = len(target)
        except TypeError:
            # TODO Probably add verification in case of value who is not an
            # list or a dict.
            return

        for i in range(0, _length - 1):
            for j in range(1, _length):
                if i != j:
                    if isinstance(target, dict):
                        keys = list(target.keys())
                        first = target[keys[i]]
                        second = target[keys[j]]
                    else:
                        first = target[i]
                        second = target[j]
                    message = f"The row {i} and {j} are the same."
                    assert first != second, self.error(message)
