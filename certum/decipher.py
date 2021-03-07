from typing import List

from certum.exception import CertumException
from certum.rule.generic.abstract import DictRule


def args_to_rule_decipher(*args) -> List[DictRule]:
    """Decipher that figures out what are the type of arguments and try to
    convert them as a list of DictRule.

    :raises CertumException: if one argument is not a DictRule complient
                             argument.
    :return: The list of dictionary rules.
    :rtype: List[DictRule]
    """
    rules = []
    for arg in args:
        if isinstance(arg, list):
            for rule in arg:
                if not isinstance(rule, DictRule):
                    raise CertumException(f"{rule} is not a dictionary rule")
                rules.append(rule)
        elif not isinstance(arg, DictRule):
            raise CertumException(f"{arg} is not a dictionary rule")
        else:
            rules.append(arg)
    return rules
