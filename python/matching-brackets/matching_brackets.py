""" Module to check if given string is valid paired bracket or parenthesis string """
PAIRS = {'[': ']', '(': ')', '{': '}'}
OPENING_BRACKETS = set(PAIRS)
CLOSING_BRACKETS = set(PAIRS.values())


def is_paired(phrase: str) -> bool:
    """ Checks if given string is valid paired bracket """
    open_stack = []
    for char in phrase:
        if char in OPENING_BRACKETS:
            open_stack.append(char)

        elif char in CLOSING_BRACKETS:
            if not open_stack or char != PAIRS[open_stack.pop()]:
                return False
    return not open_stack
