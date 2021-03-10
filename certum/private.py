from typing import Any, Dict, List

from certum.exception import CertumException
from certum.strategy.abstract import Strategy
from certum.strategy.filtering.abstract import FilteringStrategy
from certum.strategy.printing.abstract import PrintingStrategy
from certum.strategy.sorting.abstract import SortingStrategy


def _using(*args, validator: "DictValidator") -> "DictValidator":
    """Setup strategies to use by the validator. These strategies can be provided
    using :class:`certum.strategy.abstract.Strategy` or lists of
    :class:`certum.strategy.abstract.Strategy`.

    :raises CertumException: If the argument provided is not a available strategy.
    :return: Itself.
    :rtype: DictValidator
    """

    def setup_strategy(validator, strategy) -> "DictValidator":
        if isinstance(strategy, SortingStrategy):
            validator.sorting = strategy
        elif isinstance(strategy, FilteringStrategy):
            validator.filtering = strategy
        elif isinstance(strategy, PrintingStrategy):
            validator.printing = strategy
        else:
            raise CertumException("The strategy provided for the validator is unknown.")
        return validator

    for arg in args:
        if isinstance(arg, list):
            for strategy in arg:
                validator = setup_strategy(validator, strategy)
        elif isinstance(arg, Strategy):
            validator = setup_strategy(validator, arg)
        else:
            raise CertumException("The strategy provided for the validator is unknown.")

    return validator


def _target(path: List[Any], dictionary: Dict[str, Any]) -> Any:
    """Target a value following the path 'self.path' inside the dictionary.

    :Example:

    path = ["a", 0, "b"]
    obj = {"a": [{"b": 1}]}
    assert DictRule(path).target(obj) == 1 # True

    :param path: The tpath to target inside the dictionary.
    :type path: List[Any]
    :param dictionary: The targeting dictionary.
    :type dictionary: Dict[str, Any]
    :raises (TypeError, ValueError, KeyError): if the path doesn't exist.
    :return: The value of the path.
    :rtype: Any
    """
    if not path:
        return dictionary
    current = dictionary
    for key in path:
        try:
            current = current[key]
        except KeyError as error:
            path = " -> ".join(path)
            raise CertumException(f"The path '{path}' doesn't exist") from error
    return current
