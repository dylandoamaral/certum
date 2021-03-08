from dataclasses import dataclass
from typing import List

from certum.error import Error
from certum.strategy.filtering.abstract import FilteringStrategy


@dataclass
class ThunkFiltering(FilteringStrategy):
    def filter(self, errors: List[Error]) -> List[Error]:
        """Keep only the error that occurs at the minimum of depth.

        :Example:

        a -> b
        a -> 0 -> b
        a -> c
        => We keep 'a -> b' & 'a -> c'

        a -> b
        a -> 0 -> b
        a -> c
        b
        => We keep 'b'

        :param errors: The list of errors to filters.
        :type errors: List[Error]
        :return: The first error.
        :rtype: List[Error]
        """
        minimum_depth = min([len(error.path) for error in errors])
        return [error for error in errors if len(error.path) == minimum_depth]
