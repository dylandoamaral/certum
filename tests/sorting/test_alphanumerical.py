from certum.error import Error
from certum.sorting.alphanumerical import AlphanumericalSorting


def test_alphanumerical_one_depth():
    """An alphanumerical strategy should sort the messages alphanumerically for a depth
    of one."""
    errors = [Error("x", ""), Error("a", "")]
    paths = [error.path for error in AlphanumericalSorting().sort(errors)]
    assert paths == ["a", "x"]


def test_alphanumerical_two_depth():
    """An alphanumerical strategy should sort the messages alphanumerically and respects
    path ordering for multiple depth level."""
    errors = [
        Error("x", ""),
        Error("a", ""),
        Error("x -> a", ""),
        Error("x -> b", ""),
        Error("a -> b", ""),
    ]
    paths = [error.path for error in AlphanumericalSorting().sort(errors)]
    assert paths == ["a", "a -> b", "x", "x -> a", "x -> b"]


def test_alphanumerical_number():
    """An alphanumerical strategy should first show number keys then letter keys and
    respects cardinality."""
    errors = [
        Error("x", ""),
        Error("a", ""),
        Error("x -> 7.17", ""),
        Error("x -> 2", ""),
        Error("x -> 007", ""),
        Error("x -> 128", ""),
        Error("a -> 210", ""),
        Error("a -> 3", ""),
        Error("a -> a", ""),
        Error("a -> a -> b", ""),
    ]
    paths = [error.path for error in AlphanumericalSorting().sort(errors)]
    assert paths == [
        "a",
        "a -> 3",
        "a -> 210",
        "a -> a",
        "a -> a -> b",
        "x",
        "x -> 2",
        "x -> 128",
        "x -> 007",
        "x -> 7.17",
    ]
