import pytest

from certum import this
from certum.decipher import args_to_rule_decipher
from certum.exception import CertumException


def test_sucess():
    rules = args_to_rule_decipher(this.equals(2), this.has_unique_elements())
    assert len(rules) == 2


def test_failure_not_rule():
    with pytest.raises(CertumException):
        args_to_rule_decipher("a")


def test_failure_not_rule_in_list():
    with pytest.raises(CertumException):
        args_to_rule_decipher(["a"])
