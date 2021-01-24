from abc import ABC, abstractmethod
from typing import List

from certum.error import Error


class PrintingStrategy(ABC):
    @abstractmethod
    def print(self, errors: List[Error]) -> str:
        """Print a list of errors based on the printing strategy.

        :param errors: The list of errors to sort.
        :type errors: List[Error]
        :return: The stringigy version of errors.
        :rtype: str
        """
