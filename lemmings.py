"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""
    final_list = []

    for i in range(num_holes):
        worst = None
        travel = []

        for cafe in cafes:
            if worst is None:
                worst = abs(cafe - i)

            elif abs(cafe - i) < worst:
                worst = abs(cafe - i)

            travel.append(worst)
            
        final_list.append(min(travel))

    final = max(final_list)

    return final



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
