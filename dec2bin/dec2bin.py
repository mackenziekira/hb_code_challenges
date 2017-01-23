"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin(0)
    '0'

    >>> dec2bin(1)
    '1'

    >>> dec2bin(2)
    '10'

    >>> dec2bin(4)
    '100'

    >>> dec2bin(15)
    '1111'

For example, using our alternate solution::

    >>> dec2bin_forwards(0)
    '0'

    >>> dec2bin_forwards(1)
    '1'

    >>> dec2bin_forwards(2)
    '10'

    >>> dec2bin_forwards(4)
    '100'

    >>> dec2bin_forwards(15)
    '1111'

"""
from collections import deque

def dec2bin(num, base):
    """Convert a decimal number to binary representation."""
    nums = '0123456789abcdefghijklmnop'

    stack = deque()

    while num > 0:
        remainder = num % base
        stack.append(remainder)
        num = num / base

    result = ''
    while stack.__len__() > 0:
        result += nums[stack.pop()]

    if not result:
        return '0'
    return result

print dec2bin(26, 26)



# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod().failed == 0:
#         print "\n*** ALL TEST PASSED. W00T!\n"
