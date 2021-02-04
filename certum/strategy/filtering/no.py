from dataclasses import dataclass
from typing import List

from certum.error import Error
from certum.strategy.filtering.abstract import FilteringStrategy


@dataclass
class NoFiltering(FilteringStrategy):
    def filter(self, errors: List[Error]) -> List[Error]:
        """Keep all errors.

        :param errors: The list of errors to filters.
        :type errors: List[Error]
        :return: All the errors.
        :rtype: List[Error]
        """
        return errors
