"""Return new list from items with duplicates removed.

For example::

    >>> deduped([1, 1, 1])
    [1]

Keep items in the order where they first appeared::

    >>> deduped([1, 2, 1, 1, 3])
    [1, 2, 3]

A list with no duplicates would return the same::

    >>> deduped([1, 2, 3])
    [1, 2, 3]

This should return a *new* list, not mutate the existing
list::

    >>> a = [1, 2, 3]
    >>> b = deduped(a)
    >>> a == b
    True

    >>> a is b
    False

An empty list should return an empty list::

    >>> deduped([])
    []

"""


def deduped(items):
    """Return new list from items with duplicates removed."""

    #### Solution 1
    new_list = set(items)

    new_list = list(new_list)

    return new_list


    #### Solution 2
    # new_list = []

    # for item in items:
    #     if item not in new_list:
    #         new_list.append(item)

    # return new_list

    
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE NO DUPE!\n")
