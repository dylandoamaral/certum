from abc import ABC, abstractmethod
from typing import List

from certum.error import Error


class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, errors: List[Error]) -> List[Error]:
        """Sort a list of errors based on the sorting strategy.

        :param errors: The list of errors to sort.
        :type errors: List[Error]
        :return: The list of errors sorted.
        :rtype: List[Error]
        """
