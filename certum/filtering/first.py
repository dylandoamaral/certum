from dataclasses import dataclass
from typing import List

from certum.error import Error
from certum.filtering.abstract import FilteringStrategy


@dataclass
class FirstFiltering(FilteringStrategy):
    def filter(self, errors: List[Error]) -> List[Error]:
        """Keep only the first error.

        :param errors: The list of errors to filters.
        :type errors: List[Error]
        :return: The first error.
        :rtype: List[Error]
        """
        return [errors[0]]
