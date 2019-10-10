"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""

def is_prime(num):

    if num < 2:
        return False
    
    elif num == 2:
        return True
    
    elif num % 2 == 0:
        return False
    
    n = 3
    
    while n < num:
        if num % n == 0:
            return False
    
        else:
            n += 2
    
    return True


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    prime_list = []
    i = 2

    while len(prime_list) < count:

        if is_prime(i) is True:
            prime_list.append(i)
            i += 1
        
        else:
            i += 1

    return prime_list


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")
