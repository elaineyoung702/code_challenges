"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    if len(branches) == 1:
        return 0

    elif len(branches) == 2 or len(branches) == 3:
        return 1

    else:
        num_jumps = 0
        i = 0

        while i < len(branches) - 1:
            try:
                if branches[i + 2] == 0:
                    num_jumps += 1
                    i += 2

                else:
                    num_jumps += 1
                    i += 1

            except IndexError:
                if branches[i] == 0:
                    num_jumps += 1
                    i += 1

        return num_jumps


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE JUMPING!\n")