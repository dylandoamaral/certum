from typing import List

from certum.exception import CertumException
from certum.rule.generic.abstract import JsonRule


def args_to_rule_decipher(*args) -> List[JsonRule]:
    """Decipher that figures out what are the type of arguments and try to
    convert them as a list of JsonRule.

    :raises CertumException: in case one of the arguments isn't a JsonRule
                             complient argument.
    :return: The list of json rules.
    :rtype: List[JsonRule]
    """
    rules = []
    for arg in args:
        if isinstance(arg, list):
            for rule in arg:
                if not isinstance(rule, JsonRule):
                    raise CertumException(f"{rule} is not a json rule")
                rules.append(rule)
        elif not isinstance(arg, JsonRule):
            raise CertumException(f"{arg} is not a json rule")
        else:
            rules.append(arg)
    return rules
