from typing import Any, Dict

from certum.dsl import DictRuleDsl
from certum.exception import CertumException
from certum.private import _using
from certum.validator import DictValidator


def that(*args) -> DictRuleDsl:
    """Entry point to create a rule from a list of args representing the path.

    Check :class:`certum.dsl.DictRuleDsl` for the list of functions that
    generate a rule.

    :return: The dsl object that provides certum rules.
    :rtype: DictRuleDsl
    """
    return DictRuleDsl(list(args))


this = that()


def ensure(dictionary: Dict[str, Any]) -> DictValidator:
    """Entry point to analyse a dictionary object and ensure that is respects
    certain rules generate from the "that" function.

    :param dictionary: The dictionary to analyse.
    :type dictionary: Dict[str, Any]
    :return: The validator instance.
    :rtype: DictValidator
    """
    if not isinstance(dictionary, dict):
        raise CertumException("DictValidator need a dictionary of type dict.")
    return DictValidator(dictionary)


def using(*args) -> DictValidator:
    """Setup strategies to use by the validator. These strategies can be provided
    using :class:`certum.strategy.abstract.Strategy` or lists of
    :class:`certum.strategy.abstract.Strategy`.

    :raises CertumException: If the argument provided is not a available strategy.
    :return: Itself.
    :rtype: DictValidator
    """
    return _using(*args, validator=DictValidator())
