class Node(object):
    """node class

    >>> print Node(3, Node(5))
    3
    """

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)

class LinkedList(object):
    """linkedlist class"""

    def __init__(self, head):
        self.head = head

    def nth_from_last_ll(self, n):
        """returns nth from last node in linked list
        """

        first_runner = self.head
        second_runner = self.head
        i = 0
        while first_runner:
            if i >= n + 1:
                second_runner = second_runner.next
            first_runner = first_runner.next
            i += 1
        return second_runner

n1 = Node(4)
n2 = Node(5)
n3 = Node(6)

n1.next = n2
n2.next = n3

ll = LinkedList(n1)
print ll.nth_from_last_ll(2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()