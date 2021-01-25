from certum.error import Error
from certum.printing.grouped import GroupedPrinting


def test_grouped_simple():
    """A grouped strategy show a path followed by a message by default."""
    errors = [Error("x", "My message")]
    result = """x => My message\n"""
    assert GroupedPrinting().print(errors) == result


def test_grouped_one_group():
    """A grouped strategy should group messages by path."""
    errors = [
        Error("x", "My message"),
        Error("x", "My second message"),
        Error("x", "My third message very long message"),
    ]
    result = (
        "x => My message\n"
        "     My second message\n"
        "     My third message very long message\n"
    )
    assert GroupedPrinting().print(errors) == result


def test_grouped_two_group():
    """A grouped strategy should group messages by path and separate paths."""
    errors = [
        Error("x", "My message"),
        Error("x", "My second message"),
        Error("y", "My third message very long message"),
    ]
    result = (
        "x => My message\n"
        "     My second message\n"
        "y => My third message very long message\n"
    )
    assert GroupedPrinting().print(errors) == result


def test_grouped_padding():
    """A grouped strategy should add padding for smaller path length."""
    errors = [
        Error("x -> y", "My message"),
        Error("x -> y", "My second message"),
        Error("y", "My third message very long message"),
    ]
    result = (
        "x -> y => My message\n"
        "          My second message\n"
        "y      => My third message very long message\n"
    )
    assert GroupedPrinting().print(errors) == result
