from BinarySearchTree import *
from Node import *
from Debugger import *
import sys


debug = Debugger()
debug.disable()

debug.printMsg("hello, joel")
bst = BinarySearchTree("Joel")


bst.insert("34", 34)
bst.insert("43", 43)
bst.insert("51", 51)
bst.insert("12", 12)

res = bst.lookup("43")

print res.data
