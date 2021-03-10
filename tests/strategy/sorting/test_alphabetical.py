from certum.error import Error
from certum.strategy.sorting.alphabetical import AlphabeticalSorting


def test_alphabetical_one_depth():
    """An alphabetical strategy should sort the messages alphabetically for a depth of
    one."""
    errors = [Error("x", ""), Error("a", "")]
    paths = [error.path for error in AlphabeticalSorting().sort(errors)]
    assert paths == ["a", "x"]


def test_alphabetical_two_depth():
    """An alphabetical strategy should sort the messages alphabetically and respects
    path ordering for multiple depth level."""
    errors = [
        Error(["x"], ""),
        Error(["a"], ""),
        Error(["x", "a"], ""),
        Error(["x", "b"], ""),
        Error(["a", "b"], ""),
    ]
    paths = [error.path for error in AlphabeticalSorting().sort(errors)]
    assert paths == [["a"], ["a", "b"], ["x"], ["x", "a"], ["x", "b"]]


def test_alphabetical_number():
    """An alphabetical strategy don't respects cardinality."""
    errors = [
        Error(["x"], ""),
        Error(["a"], ""),
        Error(["x", 11], ""),
        Error(["x", 2], ""),
        Error(["x", 7], ""),
        Error(["x", 128], ""),
        Error(["a", 210], ""),
        Error(["a", 3], ""),
    ]
    paths = [error.path for error in AlphabeticalSorting().sort(errors)]
    assert paths == [
        ["a"],
        ["a", 3],
        ["a", 210],
        ["x"],
        ["x", 2],
        ["x", 7],
        ["x", 11],
        ["x", 128],
    ]
