from certum.exception import CertumException
from certum.strategy.abstract import Strategy
from certum.strategy.filtering.abstract import FilteringStrategy
from certum.strategy.printing.abstract import PrintingStrategy
from certum.strategy.sorting.abstract import SortingStrategy


def _using(*args, validator: "JsonValidator") -> "JsonValidator":
    """Setup strategies to use by the validator. These strategies can be provided
    using :class:`certum.strategy.abstract.Strategy` or lists of
    :class:`certum.strategy.abstract.Strategy`.

    :raises CertumException: If the argument provided is not a available strategy.
    :return: Itself.
    :rtype: JsonValidator
    """

    def setup_strategy(validator, strategy) -> "JsonValidator":
        if isinstance(strategy, SortingStrategy):
            validator.sorting = strategy
        elif isinstance(strategy, FilteringStrategy):
            validator.filtering = strategy
        elif isinstance(strategy, PrintingStrategy):
            validator.printing = strategy
        else:
            raise CertumException("The strategy provided for the validator is uknown.")
        return validator

    for arg in args:
        if isinstance(arg, list):
            for strategy in arg:
                validator = setup_strategy(validator, strategy)
        elif isinstance(arg, Strategy):
            validator = setup_strategy(validator, arg)
        else:
            raise CertumException("The strategy provided for the validator is uknown.")

    return validator
