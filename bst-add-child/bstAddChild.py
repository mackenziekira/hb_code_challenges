"""
    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.add_child(0)
    >>> t.left.left.left.data
    0

    >>> t.add_child(4)
    >>> t.right.left.left.data
    4

    >>> t.add_child(6)
    >>> t.right.right.left.data
    6
"""

class Node(object):
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def add_child(self, new):
        if new > self.data:


if __name__ == "__main__":
    import doctest
    
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NODES ADDED SUCCESSFULLY!\n"
