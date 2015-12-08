from BinarySearchTree import *
from Node import *
from Debugger import *


debug = Debugger(True)

debug.debug("hello, joel")
bst = BinarySearchTree("Joel")



bst.insert("key", 34)
bst.insert("key2", 43)

node = Node("joel", 45)

print node.isRoot()
