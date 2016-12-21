"""How much rain is trapped in Codelandia?

No buildings mean no rain is captured::

    >>> rain([])
    0

All-same height buildings capture no rain::

    >>> rain([10])
    0

    >>> rain([10, 10])
    0

    >>> rain([10, 10, 10, 10])
    0

If there's nothing between taller buildings, no rain is captured::

    >>> rain([2, 3, 10])
    0

    >>> rain([10, 3, 2])
    0

If two tallest buildings are same height and on ends, it's easy::

    >>> rain([10, 5, 10])
    5

    >>> rain([10, 2, 3, 4, 10])
    21

    >>> rain([10, 4, 3, 2, 10])
    21

    >>> rain([10, 2, 4, 3, 10])
    21

If two tallest buildings are ends, but not the same height,
it will fall off the shorter of thh two::

    >>> rain([10, 2, 3, 4, 9])
    18

Rain falls off the left and right edges::

    >>> rain([2, 3, 10, 5, 5, 10, 3, 2])
    10

Trickier::

    >>> rain([2, 3, 5, 4, 3, 10, 7, 10, 5, 4, 3, 6, 2, 5, 2])
    15

Should also work with floats::

    >>> r = rain([4.5, 2.2, 2.2, 4])
    >>> round(r, 2)
    3.6
"""


def rain(buildings):
    """How much rain is trapped in Codelandia?"""

    if not buildings:
        return 0

    dam_indicies = []

    for index in xrange(0, len(buildings) - 1):
        current = buildings[index]
        next = buildings[index + 1]

        if current > next and not dam_indicies:
            print 'a'
            dam_indicies.append(index)
        elif current > next and current >= buildings[dam_indicies[-1]] and index != dam_indicies[-1]:
            print 'b'
            dam_indicies.append(index)
        elif current < next and not dam_indicies:
            print 'c'
            continue
        elif current < next and next > buildings[dam_indicies[-1]] and len(dam_indicies) > 1:
            print 'd'
            dam_indicies.pop()
            dam_indicies.append(index + 1)
        elif current < next:
            print 'e'
            dam_indicies.append(index + 1)


    print dam_indicies



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
