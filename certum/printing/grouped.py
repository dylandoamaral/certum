from collections import OrderedDict
from dataclasses import dataclass
from typing import Dict, List

from certum.error import Error
from certum.printing.abstract import PrintingStrategy


@dataclass
class GroupedPrinting(PrintingStrategy):

    key_separator: str = " -> "

    def print(self, errors: List[Error]) -> str:
        """Print a list of errors based on the printing strategy.

        The grouped strategy group path by keys and add tabulation to align all paths
        together.

        :param errors: The list of errors to sort.
        :type errors: List[Error]
        :return: The stringigy version of errors.
        :rtype: str
        """
        path_lengths = [len(error.path) for error in errors]
        max_path_length = max(path_lengths)

        grouped_errors: Dict[str, List[str]] = OrderedDict()
        for error in errors:
            try:
                grouped_errors[error.path] += [error.message]
            except KeyError:
                grouped_errors[error.path] = [error.message]

        message = ""
        for path, errors in grouped_errors.items():
            spaces = max_path_length - len(path)
            str_path = path + " " * spaces
            message += f"{str_path} => {errors[0]}\n"
            for error in errors[1:]:
                message += " " * (max_path_length + 4) + error + "\n"
        return message
