from typing import Any, Dict

from certum.dsl import JsonRuleDsl
from certum.exception import CertumException
from certum.private import _using
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
    path = path.split(" -> ") if path else []
    return JsonRuleDsl(path)


this = that("")


def ensure(json: Dict[str, Any]) -> JsonValidator:
    """Entry point to analyse a json object and ensure that is respects
    certain rules generate from the "that" function.

    :param json: The json to analyse.
    :type json: Dict[str, Any]
    :return: The validator instance.
    :rtype: JsonValidator
    """
    if not isinstance(json, dict):
        raise CertumException("JsonValidator need a json of type dict.")
    return JsonValidator(json)


def using(*args) -> JsonValidator:
    """Setup strategies to use by the validator. These strategies can be provided
    using :class:`certum.strategy.abstract.Strategy` or lists of
    :class:`certum.strategy.abstract.Strategy`.

    :raises CertumException: If the argument provided is not a available strategy.
    :return: Itself.
    :rtype: JsonValidator
    """
    return _using(*args, validator=JsonValidator())
