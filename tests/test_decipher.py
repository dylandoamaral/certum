import pytest

from certum import this
from certum.decipher import args_to_rule_decipher
from certum.exception import CertumException


def test_sucess():
    """Ensure that the decipher function can extract rules from arguments."""
    rules = args_to_rule_decipher(this.equals(2), this.has_unique_elements())
    assert len(rules) == 2


def test_sucess_array():
    """Ensure that the decipher function can extract rules from list."""
    rules = args_to_rule_decipher([this.equals(2), this.has_unique_elements()])
    assert len(rules) == 2


def test_failure_not_rule():
    """Ensure that the decipher should not extract argument that are not
    rules and raise a :class:`certum.exception.CertumException`."""
    with pytest.raises(CertumException):
        args_to_rule_decipher("a")


def test_failure_not_rule_in_list():
    """Ensure that the decipher should not extract argument inside a list that
    are not rules and raise a :class:`certum.exception.CertumException`."""
    with pytest.raises(CertumException):
        args_to_rule_decipher(["a"])
