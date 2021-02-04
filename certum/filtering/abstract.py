from abc import ABC, abstractmethod
from typing import List

from certum.error import Error


class FilteringStrategy(ABC):
    @abstractmethod
    def filter(self, errors: List[Error]) -> List[Error]:
        """Filter a list of errors based on the filtering strategy.

        :param errors: The list of errors to filters.
        :type errors: List[Error]
        :return: The errors filtered.
        :rtype: List[Error]
        """
