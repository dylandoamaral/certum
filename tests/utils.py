import string
from random import choice, randint
from typing import List

from certum.error import Error
from certum.exception import CertumException


def assert_error(error: CertumException, message: str):
    """Assert a CertumException exception message wrapping the error message
    for me.

    :param error: The exception.
    :type error: :class:`certum.exception.CertumException`
    :param message: The message that should be throwed.
    :type message: str
    """
    assert error.value.args[0] == f"\n\n{message}\n"


def generate_errors(number_of_errors: int, depth: int) -> List[Error]:
    """Generate a large number of random errors.

    :param number_of_errors: The number of errors to generate.
    :type number_of_errors: int
    :param depth: The path depth of the generated input, this is a maximum so you can
                  have a path with a lower depth.
    :type depth: int
    :return: [description]
    :rtype: List[Error]
    """
    errors = []
    for _ in range(0, number_of_errors):
        possibilities = string.ascii_letters + str(range(0, 20))
        keys = [choice(possibilities) for i in range(0, randint(1, depth))]
        errors.append(Error(" -> ".join(keys), ""))
    return errors
