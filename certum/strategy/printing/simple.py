from dataclasses import dataclass
from typing import List

from certum.error import Error
from certum.strategy.printing.abstract import PrintingStrategy


@dataclass
class SimplePrinting(PrintingStrategy):

    key_separator: str = " -> "

    def print(self, errors: List[Error]) -> str:
        """Print a list of errors based on the printing strategy.

        :param errors: The list of errors to sort.
        :type errors: List[Error]
        :return: The stringigy version of errors.
        :rtype: str
        """
        message = ""
        for error in errors:
            path = self.key_separator.join(error.path)
            message += f"[{path}] => {error.message}\n"
        return message
