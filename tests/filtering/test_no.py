from certum.filtering.no import NoFiltering
from tests.utils import generate_errors


def test_no():
    """A no filtering strategy should not filter."""
    errors = generate_errors(10, 5)
    assert NoFiltering().filter(errors) == errors
