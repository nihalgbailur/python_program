# how to check whether the given variable is keyword or not.

import keyword
def is_keyword(var):
    if var in keyword.kwlist:
        return True
    else:
        return False


print(is_keyword("self"))

