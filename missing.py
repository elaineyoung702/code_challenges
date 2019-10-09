"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """
    nums = set(nums)

    i = 1

    while i < max_num:
        if i not in nums:
            return i
        i += 1


    ####### First solution
    # nums = set(nums)

    # for i in range(max_num):
    #     if i == 0:
    #         continue
    #     if i not in nums:
    #         return i


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
