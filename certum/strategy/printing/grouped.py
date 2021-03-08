from collections import OrderedDict
from dataclasses import dataclass
from typing import Dict, List

from certum.error import Error
from certum.strategy.printing.abstract import PrintingStrategy


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
        max_path_length = -1
        grouped_errors: Dict[str, List[str]] = OrderedDict()
        for error in errors:
            path = self.key_separator.join(error.path)
            if len(path) > max_path_length:
                max_path_length = len(path)
            try:
                grouped_errors[path] += [error.message]
            except KeyError:
                grouped_errors[path] = [error.message]

        message = ""
        for path, errors in grouped_errors.items():
            spaces = max_path_length - len(path)
            str_path = path + " " * spaces
            message += f"{str_path} => {errors[0]}\n"
            for error in errors[1:]:
                message += " " * (max_path_length + 4) + error + "\n"
        return message
