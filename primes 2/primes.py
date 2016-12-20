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
        if is_prime(i):
            result.append(i)
        lng = len(result)
        i += 1

    return result

def is_prime(num):
    # end = int(sqrt(num))
    # print end
    for x in xrange(2, num):
        if num % x == 0:
            return False
    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
