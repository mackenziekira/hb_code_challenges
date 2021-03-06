"""Boggle word check.

Given a 5x5 boggle board, see if you can find a given word in it.

In Boggle, you can start with any letter, then move in any NEWS direction.
You can continue to change directions, but you cannot use the exact same
tile twice.

So, for example::

    N C A N E
    O U I O P
    Z Q Z O N
    F A D P L
    E D E A Z
 
In this grid, you could find `NOON* (start at the `N` in the top
row, head south, and turn east in the third row). You cannot find
the word `CANON` --- while you can find `CANO` by starting at the
top-left `C`, you can 't re-use the exact same `N` tile on the
front row, and there's no other `N` you can reach.

For example::

    >>> board = make_board('''
    ... N C A N E
    ... O U I O P
    ... Z Q Z O N
    ... F A D P L
    ... E D E A Z
    ... ''')

`NOON` should be found (0, 3) -> (1, 3) -> (2, 3) -> (2, 4)::
 
    >>> find(board, "NOON")
    True

`NOPE` should be found (0, 3) -> (1, 3) -> (1, 4) -> (0, 4)::

    >>> find(board, "NOPE")
    True

`CANON` can't be found (`CANO` starts at (0, 1) but can't find
the last `N` and can't re-use the N)::

    >>> find(board, "CANON")
    False

You cannot travel diagonally in one move, which would be required
to find `QUINE`::

    >>> find(board, "QUINE")
    False

We can recover if we start going down a false path (start 3, 0)::

    >>> find(board, "FADED")
    True

    >>> board = make_board('''
    ... N C A N E
    ... O U I O P
    ... Z Q Z O N
    ... F A D P L
    ... E D E A Z
    ... ''')

    >>> board2 = make_board('''
    ... E D O S Z
    ... N S O N R
    ... O U O O P
    ... Z Q Z O R
    ... F A D P L
    ... ''')

    >>> find(board2, "NOOOOS")
    True
"""


def make_board(board_string):
    """Make a board from a string.

    For example::

        >>> board = make_board('''
        ... N C A N E
        ... O U I O P
        ... Z Q Z O N
        ... F A D P L
        ... E D E A Z
        ... ''')

        >>> len(board)
        5

        >>> board[0]
        ['N', 'C', 'A', 'N', 'E']
    """

    letters = board_string.split()

    board = [
        letters[0:5],
        letters[5:10],
        letters[10:15],
        letters[15:20],
        letters[20:25],
    ]

    return board

def find_from(board, word, row, col, seen = None):
    """ Returns True if this is a valid case """


    # print "coor: row:%i ----- col:%i " %(row,col)
    # print "seen: ",
    # print seen
    # print "word: %s" %word


    if not seen:
        seen = set()

    if (row,col) in seen:
        return False

    if len(word) == 0:
        return True
  
        
    seen.add((row,col))


    # look right
    if col < 4 and board[row][col+1] == word[0]:
        seen.add((row, col+1))
        if find_from(board, word[1:], row, col+1, seen):
            return True
        else:
            seen.remove((row, col+1))

    # look left
    if col > 0 and board[row][col-1] == word[0]:
        seen.add((row, col-1))
        if find_from(board, word[1:], row, col-1, seen):
            return True
        else:
            seen.remove((row, col-1))

    # look up
    if row > 0 and board[row-1][col] == word[0]:
        seen.add((row-1, col))
        if find_from(board, word[1:], row-1, col, seen):
            return True
        else:
            seen.remove((row-1, col))


    # look down
    if row < 4 and board[row+1][col] == word[0]:
        seen.add((row+1, col))
        if find_from(board, word[1:], row+1, col, seen):
            return True
        else:
            seen.remove((row+1, col))


    return False


def find(board, word):
    """Can word be found in board?"""

    for row in range(5):
        for col in range(5):
            if word[0] == board[row][col]:
                if find_from(board, word[1:], row, col):
                    return True
    return False



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; YOU FOUND SUCCESS! ***\n"
