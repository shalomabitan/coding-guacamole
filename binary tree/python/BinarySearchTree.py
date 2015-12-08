from Node import *


class BinarySearchTree(object):
    """A Binary Search Tree Implementation:

    Attributes:
        name: A string representing the BST's name.
        Root: A root node which gets initialized to None.
    """

    def __init__(self, name):
        """Create the root node of the BST.
        """
        self.name = name
        self.root = None
        self.size = 0

    def length(self):
        """Returns the length of the BST
        """
        return self.length

    def __len__(self):
        """internal function returns length
        """
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def insert(self, key, data):
        """This function will insert 
            data into the BST using a log_2(n)
            algorithm
        """
        # if there is no root node
        if not self.root:
            self.root = Node(key, data)
        else:
            self.recursiveInsert(key,val,self.root)
        # increment the size of the BST
        self.size = self.size + 1

    def recursiveInsert(self, key, value, parent):
        """This is the main algorithm for insert
        """
        pass
