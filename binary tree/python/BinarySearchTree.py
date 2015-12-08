from Node import *
from Debugger import *


# init the debugger
debug = Debugger()
debug.enable()

class BinarySearchTree(object):
    """A Binary Search Tree Implementation:

    Attributes:
        name: A string representing the BST's name.
        Root: A root node which gets initialized to None.
    """

    def __init__(self, name):
        """Create the root node of the BST.
        """
        debug.printMsg("We Initiated a BST with no root node")
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

    def __setitem__(self,k,v):
        """Allows to override how we insert things"""
        self.insert(k,v)

    def insert(self, key, data):
        """This function will insert 
            data into the BST using a log_2(n)
            algorithm
        """
        debug.printMsg('Insert for "' + key + '" With data: ' + str(data) )
        # if there is no root node
        if not self.root:
            debug.printMsg("No root was found, create one")
            self.root = Node(key, data)
        else:
            self.recursiveInsert(key, data, self.root)
        # increment the size of the BST
        self.size = self.size + 1

    def recursiveInsert(self, key, data, curr):
        """This is the main algorithm for insert
        """
        # check if the key is greater than current node key
        # we will go right
        if key > curr.key:
            # now check if there is a right node already
            if curr.hasRightChild():
                # well, we're shit out of luck and need to go further
                self.recursiveInsert(key, data, curr.right)
            else:
                # we found an empty spot
                curr.right = Node(key, data, curr)
        else:
             # now check if there is a left node already
            if curr.hasLeftChild():
                # well, we're shit out of luck and need to go further
                self.recursiveInsert(key, data, curr.left)
            else:
                # we found an empty spot
                curr.left = Node(key, data, curr)

