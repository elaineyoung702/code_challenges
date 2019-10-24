"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """

    ab_list = []

    while a and b:
        if a[0] < b[0]:
            ab_list.append(a[0])
            a.pop(0)
        else:
            ab_list.append(b[0])
            b.pop(0)

    if not a and not b:
        return ab_list 

    if not a:
        ab_list.extend(b)

    if not b:
        ab_list.extend(a)

    return ab_list


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n")
