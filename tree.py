"""Tree class and tree node class.

Discussion Questions:

1. Food - Italian - Indian - Mexican - lasagna - pizza - tikka masala - saag - burritos

2. Food - Mexican - enchiladas - tacos - burritos - Indian - saag - tikka masala -
   Italian - pizza - Sicilian - New York-style - Chicago-style

3. A binary search tree has a search runtime of O(log n). This is possible because
each node in a binary search tree has two children, right and left, that are assigned
according to relation to the node. When traversing the list, choosing right or left
effectively eliminates half of the remaining options, reducing the number of potential
operations in worst case."""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node %s>" % self.data

    def get_num_children(self):
        """Get number of children.

        For example::

            >>> a = Node("A", [Node("B"), Node("C")])
            >>> a.get_num_children()
            2
        """

        return len(self.children)


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root=%s>" % self.root

    def depth_first_search(self, data):
        """Return node object with this data, traversing the tree depth-first.

        Start at the root, and return None if not found.
        """

        to_visit = [self.root]

        while to_visit:
            node = to_visit.pop()

            if node.data == data:
                return node

            to_visit.extend(node.children)

    def breadth_first_search(self, data):
        """Return node object with this data, traversing the tree breadth-first.

        Start here (on this node), and return None if not found.

        Let's make a tree where we have two "B" nodes, but where one is far down an
        earlier branch and the other is higher-up in an earlier branch. Since this is
        a BFS, we should find the b2 node for "B"::

                       A
                     /   \
                    C     E
                   /       \
                  D        B2
                 /
                B1

            >>> a = Node("A")
            >>> b1 = Node("B")
            >>> b2 = Node("B")
            >>> c = Node("C")
            >>> d = Node("D")
            >>> e = Node("E")
            >>> a.children = [c, e]
            >>> c.children = [d]
            >>> d.children = [b1]
            >>> e.children = [b2]
            >>> tree = Tree(a)

            >>> tree.breadth_first_search("B") is b2
            True

        """

        current = self.root
        to_check = [current]

        while to_check:
            current = to_check.pop(0)
            if current.data == data:
                return current
            to_check.extend(current.children)

        return False

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
