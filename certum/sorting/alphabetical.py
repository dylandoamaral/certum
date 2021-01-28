from typing import List
from dataclasses import dataclass

from certum.error import Error
from certum.sorting.abstract import SortingStrategy


@dataclass
class AlphabeticalSorting(SortingStrategy):
    def sort(self, errors: List[Error]) -> List[Error]:
        """Sort a list of errors alphabeticaly.

        This is a simple algorithm that works perfectly with alphabetical key.
        However it is not advised when you have numerical keys such as array index
        because it will sort these keys according to the alphabetical order and not
        numerical order.

        :Example:

        1, 2, 10, 101 will become 1, 10, 101, 2

        :param errors: The list of errors to sort.
        :type errors: List[Error]
        :return: The list of errors sorted.
        :rtype: List[Error]
        """
        return sorted(errors, key=lambda error: "".join(error.path))
