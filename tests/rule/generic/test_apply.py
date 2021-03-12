from typing import Any, Dict, List

import pytest

from certum import ensure, that
from certum.exception import CertumException
from certum.rule.generic.apply import DictRuleApply
from tests.utils import assert_error


def fn(value: Any) -> List[str]:
    """The function of apply.

    :param value: The targeted value
    :type value: Any
    :return: [description]
    :rtype: List[Error]
    """
    if value == 1:
        return []
    return [f"{value} != 1."]


def test_apply_success():
    """Ensuring that you can apply a function correctly."""
    obj = {"x": 1}
    validator = ensure(obj).respects(that("x").apply(fn))
    validator.check()


def test_apply_fail():
    """Ensuring that you can apply a function correctly."""
    obj = {"x": 2}
    validator = ensure(obj).respects(that("x").apply(fn))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => 2 != 1.")
