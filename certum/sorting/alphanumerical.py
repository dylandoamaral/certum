from typing import List, Tuple, Union

from certum.error import Error
from certum.sorting.abstract import SortingStrategy


class AlphanumericalSorting(SortingStrategy):
    def sort(self, errors: List[Error]) -> List[Error]:
        """Sort a list of errors alphabeticaly and taking number into account.

        This is a loosely algorithm, can surely be improved.

        :param errors: The list of errors to sort.
        :type errors: List[Error]
        :return: The list of errors sorted.
        :rtype: List[Error]
        """
        fragmented_errors: Tuple[List[str], str] = [
            (error.path.split(" -> "), error.message) for error in errors
        ]
        depth = max([len(error[0]) for error in fragmented_errors])
        error_table: List[List[Union[float, str]]] = []

        for error in fragmented_errors:
            row: List[Union[float, str]] = []
            for key in error[0]:
                try:
                    if len(key) > 1 and key[0] == "0":
                        raise ValueError
                    if float(key).is_integer():
                        row.append(int(key))
                    else:
                        row.append(key)
                except ValueError:
                    row.append(key)
            row += [None] * (depth - len(error[0])) + [error[1]]
            error_table.append(row)

        for current_depth in range(depth - 1, -1, -1):
            error_table = sorted(
                error_table,
                key=lambda error: (
                    error[current_depth] is not None,
                    isinstance(error[current_depth], str),
                    error[current_depth],
                ),
            )

        sorted_errors: List[Error] = []
        for row in error_table:
            keys = [str(key) for key in row[:-1] if key is not None]
            message = row[-1]
            sorted_errors.append(Error(" -> ".join(keys), message))

        return sorted_errors
