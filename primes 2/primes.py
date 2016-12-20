"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""
from math import sqrt

def primes(count):
    """Return count number of prime numbers, starting at 2."""

    result = []
    lng = len(result)
    i = 2

    while lng < count:
        for num in xrange(2, i):
            if i % num == 0:
                i += 1
                break
        result.append(i)
        lng = len(result)
        i += 1

    return result


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
