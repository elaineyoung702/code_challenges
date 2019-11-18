"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""

    s = s.split(" ")
    num1 = s[-1]
    num2 = s[-2]
    if s[-3] == "+":
        final_val = int(num1) + int(num2)
    elif s[-3] == "-":
        final_val = int(num2) - int(num1)
    elif s[-3] == "*":
        final_val = int(num1) * int(num2)
    elif s[-3] == "/":
        final_val = int(num2) / int(num1)

    if len(s) <= 3:
        return final_val

    num3 = s[1]

    if s[0] == "+":
        final_val += int(num3)
    elif s[0] == "-":
        final_val = int(num3) - final_val
    elif s[0] == "*":
        final_val = final_val * int(num3)
    elif s[0] == "/":
        final_val = int(num3) / final_val

    return int(final_val)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")
