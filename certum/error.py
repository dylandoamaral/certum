from dataclasses import dataclass
from typing import List


@dataclass
class Error:
    """An error returned by a rule that need to be sorted and showed to the
    user."""

    path: List[str]
    message: str
