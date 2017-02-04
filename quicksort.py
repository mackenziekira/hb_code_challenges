def quicksort(lst):
    """
    >>> quicksort([5, 7, 3, 9, 10, 2, 1])
    [1, 2, 3, 5, 7, 9, 10]
    """
    return partition(lst, 0, len(lst))

def partition(lst, left, right):
    """
    >>> partition([5, 7, 3, 9, 10, 2, 1], 0, 7)
    [1, 2, 3, 5, 7, 9, 10]
    """
    if abs(right - left) < 2:
        return

    pivot = lst[left]

    split = left + 1

    j = left + 1

    while j < right:
        if pivot > lst[j]:
            lst[split], lst[j] = lst[j], lst[split]
            split += 1
        j += 1

    lst[left], lst[split - 1] = lst[split - 1], lst[left]

    partition(lst, left, split)
    partition(lst, split, right)

    return lst


if __name__ == "__main__":
    import doctest
    doctest.testmod()