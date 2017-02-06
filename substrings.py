def substr(s):
    """returns all substrings of string s in alphabetical order

    >>> substr('ba')
    ['a', 'b', 'ba']

    >>> substr('abc')
    ['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
    """
    res = set()
    for i in xrange(0, len(s)):
        j = i + 1
        while j < len(s) + 1:
            for k in xrange(j, len(s) + 1):
                my_str = s[i] + s[j:k]
                res.add(my_str)
            j += 1
    return sorted(list(res))


if __name__ == "__main__":
    import doctest
    doctest.testmod()