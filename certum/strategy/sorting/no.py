from typing import List

from certum.error import Error
from certum.strategy.sorting.abstract import SortingStrategy


class NoSorting(SortingStrategy):
    def sort(self, errors: List[Error]) -> List[Error]:
        """Don't sort errors.

        :param errors: The list of errors to sort.
        :type errors: List[Error]
        :return: The list of errors sorted.
        :rtype: List[Error]
        """
        return errors
