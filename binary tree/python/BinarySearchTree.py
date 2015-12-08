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
            debug.printMsg("Root was found, starting recursive insert")
            self.recursiveInsert(key, data, self.root)
        # increment the size of the BST
        debug.printMsg("Incrementing size of BST")
        self.size = self.size + 1

    def recursiveInsert(self, key, data, curr):
        """This is the main algorithm for insert
        """
        debug.printMsg("Entered recursiveInsert")
        # check if the key is greater than current node key
        # we will go right
        debug.printMsg("checking whether we go right or left")
        if key > curr.key:
            debug.printMsg("we go right")
            # now check if there is a right node already
            debug.printMsg("checking if we have available space")
            if curr.hasRightChild():
                debug.printMsg("nope, calling recursiveInsert again")
                # well, we're shit out of luck and need to go further
                self.recursiveInsert(key, data, curr.right)
            else:
                debug.printMsg("yep, we'll insert it here")
                # we found an empty spot
                curr.right = Node(key, data, curr)
        else:
            debug.printMsg("we go left")
             # now check if there is a left node already
            if curr.hasLeftChild():
                debug.printMsg("checking if we have available space")
                # well, we're shit out of luck and need to go further
                self.recursiveInsert(key, data, curr.left)
            else:
                # we found an empty spot
                debug.printMsg("yep, we'll insert it here")
                curr.left = Node(key, data, curr)

    def lookup(self, key):
        """Gets a specific key from the BST
        """
        # check that this tree actually has a root node
        debug.printMsg("Call made to Lookup")
        debug.printMsg("checking if we have a BST")
        if self.root:
            debug.printMsg("Calling Recursive Lookup")
            (result, err) = self.recursiveLookup(key, self.root)
            # if we did not find anything
            if err: 
                debug.printMsg("Oops, we couldn't find anything")
                return None
            else: 
                # we found a result
                debug.printMsg("we found: ")
                return result
        else:
            debug.printMsg("Oops, the BST seems to not exist")
            # root doesnt exist
            return None

    def recursiveLookup(self, key, curr):
        """Recusrisvely searched the BST using log_2(n) algorithm to 
        find the key is there is
        """
        # basically repeat insert
    
        # if we found a match break
        if key == curr.key:
            return (curr, None)
        # if the key is larger than curr
        elif key > curr.key:
            if curr.hasRightChild():
                # move onto the next node along the search path
                return self.recursiveLookup(key, curr.right)
            else:
                # hit the end and there was no match
                return (None, True)
            if curr.hasLeftChild():
                return self.recursiveLookup(key, curr.left)
            else:
                return (None, True)









