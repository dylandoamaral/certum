import operator
from typing import List

from certum.error import Error
from certum.sorting.abstract import SortingStrategy


class AlphabeticalSorting(SortingStrategy):
    def sort(self, errors: List[Error]) -> List[Error]:
        """Sort a list of errorsalphabeticaly.

        :param errors: The list of errors to sort.
        :type errors: List[Error]
        :return: The list of errors sorted.
        :rtype: List[Error]
        """
        return sorted(errors, key=operator.attrgetter("path"))
