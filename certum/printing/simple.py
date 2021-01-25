from typing import List

from certum.error import Error
from certum.printing.abstract import PrintingStrategy


class SimplePrinting(PrintingStrategy):
    def print(self, errors: List[Error]) -> str:
        """Print a list of errors based on the printing strategy.

        :param errors: The list of errors to sort.
        :type errors: List[Error]
        :return: The stringigy version of errors.
        :rtype: str
        """
        message = ""
        for error in errors:
            message += f"[{error.path}] => {error.message}\n"
        return message
