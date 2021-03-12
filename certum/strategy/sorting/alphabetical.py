from dataclasses import dataclass
from typing import Any, List, Tuple

from certum.error import Error
from certum.strategy.sorting.abstract import SortingStrategy


@dataclass
class AlphabeticalSorting(SortingStrategy):
    def sort(self, errors: List[Error]) -> List[Error]:
        """Sort a list of errors alphabeticaly.

        :param errors: The list of errors to sort.
        :type errors: List[Error]
        :return: The list of errors sorted.
        :rtype: List[Error]
        """

        def _key(index: int) -> Tuple[bool, Any]:
            def __key(error: Error) -> Tuple[bool, Any]:
                """Create a tuple to help sorting the errors.

                :param error: The error to sort.
                :type error: Error
                :return: The sorting keys composed by a tuple of two elements, if the
                         index exists and the value for this index.
                :rtype: Tuple[bool, Any]
                """
                try:
                    value = error.path[index]
                    return True, value
                except IndexError:
                    return False, ""

            return __key

        max_path_lengths = max([len(error.path) for error in errors])

        errors = sorted(errors, key=lambda error: error.message)

        for index in range(max_path_lengths - 1, -1, -1):
            errors = sorted(errors, key=_key(index))

        return errors
