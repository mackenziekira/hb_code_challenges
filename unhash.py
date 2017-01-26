


def myhash(s):
    """hash a string

    >>> myhash('leepadg')
    680131659347
    """

    result = 7
    letters = "acdegilmnoprstuw"

    for i in xrange(len(s)):
        result = result * 37 + letters.index(s[i])

    return result

def unhash(x, len_str):
    """unhash a number

    >>> unhash(680131659347, 7)
    'leepadg'
    """

    result = x
    letters = "acdegilmnoprstuw"

    for i in xrange(len_str - 1, -1, -1):
        result = (result - letters.index([i])) / 37

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()