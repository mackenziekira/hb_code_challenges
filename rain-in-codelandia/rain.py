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

    dams = []

    skyline = len(buildings) - 1
    at_end = skyline - 1

    for building_index in xrange(skyline):
        current_building = buildings[building_index]
        next_building = buildings[building_index + 1]

        if current_building > next_building:
            if not dams:
                dams.append(building_index)
            elif len(dams) > 1 and current_building > buildings[dams[-1]]:
                dams.pop()
                dams.append(building_index)
            elif current_building > buildings[building_index - 1]:
                dams.append(building_index)
        elif next_building > current_building: 
            if building_index == at_end:
                if len(dams) > 1 and next_building > buildings[dams[-1]]:
                    dams.pop()
                dams.append(building_index + 1)
 


    levee_1 = 0
    levee_2 = 1
    num_dams = len(dams)
    total_water = 0

    while levee_2 < num_dams:
        lowest_levee = min(buildings[dams[levee_1]], buildings[dams[levee_2]])
        for building_index in xrange(dams[levee_1] + 1, dams[levee_2]):
            total_water += lowest_levee - buildings[building_index]
        levee_1 += 1
        levee_2 += 1

    return total_water



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
