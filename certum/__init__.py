from typing import Any, Dict

from certum.dsl import JsonRuleDsl
from certum.validator import JsonValidator


def that(path: str) -> JsonRuleDsl:
    """Entry point to create a rule from the path.

    Check :class:`certum.dsl.JsonRuleDsl` for the list of functions that
    generate a rule.

    :param path: The path where the rule should be applied.
    :type path: str
    :return: The dsl object that provides certum rules.
    :rtype: JsonRuleDsl
    """
    return JsonRuleDsl(path)


this = that("")


def ensure(json: Dict[str, Any]) -> JsonValidator:
    """Entry point to analyse a json object and ensure that is respects
    certain rules generate from the "that" function.

    :param json: The json to analyse.
    :type json: Dict[str, Any]
    :return: The
    :rtype: JsonValidator
    """
    return JsonValidator(json)
