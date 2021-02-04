from abc import ABC, abstractmethod
from typing import List

from certum.error import Error


class PrintingStrategy(ABC):
    @abstractmethod
    def print(self, errors: List[Error]) -> str:
        """Print a list of errors based on the printing strategy.

        :param errors: The list of errors to print.
        :type errors: List[Error]
        :return: The stringify version of errors.
        :rtype: str
        """
