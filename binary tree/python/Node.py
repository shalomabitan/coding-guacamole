class Node(object):
	"""A Binary Search Tree Node Implementation:

    Attributes:
        Key: A string representing the Node's name.
        Data: The information that you want to place in the Binary search tree.
        leftNode: The pointer to the left node

    """

	def __init__(self, key, data, leftNode = None, rightNode = None, parentNode = None):
		"""The TreeNode takes a key and data pair, in addition
		   an optional left, right and parent pointer
		"""
		self.left = leftNode
		self.right = rightNode
		self.parent = parentNode
		self.key = key
		self.data = data

	def hasLeftChild(self):
		"""Checks whether this TreeNode has a leftChild
		"""
		return self.left

	def hasRightChild(self):
		"""Checks whether this TreeNode has a rightChild
		"""
		return self.Reft

	def isLeftChild(self):
		"""Checks whether this node is a leftChild
		"""
		return self.parent and self.parent.left == self

    def isRightChild(self):
    	"""Checks whether this node is a rightChild
		"""
		return self.parent and self.parent.right == self

    def isRoot(self):
    	"""checks if this is the root node
    	"""
    	return not self.parent

    def isLeaf(self):
    	"""Checks whether this is a leaf (no children)
    	"""
    	return not (self.right or self.left)

    def hasAnyChildren(self):
    	"""Checks whether this is not a leaf
    	"""
    	return self.right or self.left

    def isComplete(self):
    	"""checks is this node is complete
    	"""
    	return self.right and self.left

   	def updateNode(self, key, data, leftNode, rightNode):
   		"""Updates the node with the appropriate data
   		"""
   		self.key = key
        self.data = data
        self.left = leftNode
        self.right = rightNode
        # if this node has a left child update it
        if self.hasLeftChild():
            self.left.parent = self
        #if this node has right child update parent pointer 
        if self.hasRightChild():
            self.right.parent = self