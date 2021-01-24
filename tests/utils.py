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
