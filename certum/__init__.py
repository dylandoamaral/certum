from typing import Any, Dict

from certum.dsl import JsonRuleDsl
from certum.validator import JsonValidator


def that(path: str) -> JsonRuleDsl:
    return JsonRuleDsl(path)


this = JsonRuleDsl("")


def ensure(json: Dict[str, Any]) -> JsonValidator:
    return JsonValidator(json)
