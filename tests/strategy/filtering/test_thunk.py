import pytest

from certum.error import Error
from certum.strategy.filtering.thunk import ThunkFiltering


@pytest.mark.parametrize(
    "errors, result",
    [
        ([Error(["x"], "my message")], 1),
        ([Error(["x", "b"], "my message")], 1),
        ([Error(["x"], "my message"), Error(["x", "b"], "my message")], 1),
        (
            [
                Error(["x"], "my message"),
                Error(["x", "b"], "my message"),
                Error(["x", "b", "e"], "my message"),
            ],
            1,
        ),
        (
            [
                Error(["x"], "my message"),
                Error(["x", "b"], "my message"),
                Error(["y"], "my message"),
            ],
            2,
        ),
    ],
)
def test_thunk(errors, result):
    """A thunk filtering strategy should keep the elements with the minimum depth."""
    assert len(ThunkFiltering().filter(errors)) == result
