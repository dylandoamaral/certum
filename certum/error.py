from dataclasses import dataclass


@dataclass
class Error:
    """An error returned by a rule that need to be sorted and showed to the
    user."""

    path: str
    message: str
