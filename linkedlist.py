"""Linked list with Node/LinkedList classes.

Discussion Questions:

1. The nodes are the boxes, including the data and next attributes.
   The data for each node is the box containing the string.
   The head is an attribute of the linked list pointing to the first node.
   The tail is an optional attribute of the linked list pointing to the last node.

2. A singly-linked list is a list in which each node has a next attribute that
points to the node directly following it. A doubly-linked list has both a next
and prev attribute, the latter of which points to the node directly preceding it.

3. Without a tail attribute, the entire list must be traversed in order to find
the last item and append to it. The presence of the tail attribute provides a
quick jumping mechanism to a significant location in the list.
"""


class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node %s>" % self.data


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        """Add node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def remove_node_by_index(self, index):
        """Remove node with given index."""

        prev = None
        node = self.head
        i = 0

        while (node is not None) and (i < index):
            prev = node
            node = node.next
            i += 1

        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next

    def find_node(self, data):
        """Is a matching node in the list?"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def print_list(self):
        """Print all items in the list::

            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('fish')

            >>> ll.print_list()
            dog
            cat
            fish
        """

        current = self.head

        while current is not None:
            print current.data
            current = current.next

    def get_node_by_index(self, idx):
        """Return a node with the given index::

            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('fish')

            >>> ll.get_node_by_index(0)
            <Node dog>

            >>> ll.get_node_by_index(2)
            <Node fish>
        """

        current = self.head
        i = 0

        while (current is not None) and (i < idx):
            current = current.next
            i += 1

        return current

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
