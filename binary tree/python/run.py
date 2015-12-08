from BinarySearchTree import *
from Node import *
from Debugger import *
import sys


debug = Debugger()
debug.disable()

debug.printMsg("hello, joel")
bst = BinarySearchTree("Joel")



bst.insert("key", 34)
bst.insert("key2", 43)

node = Node("joel", 45)

print node.isRoot()
