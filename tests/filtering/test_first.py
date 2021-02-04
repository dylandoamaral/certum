from certum.filtering.first import FirstFiltering
from tests.utils import generate_errors


def test_first():
    """A first filtering strategy should keep the first element."""
    errors = generate_errors(10, 5)
    assert FirstFiltering().filter(errors) == [errors[0]]
