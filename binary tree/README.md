#Binary Tree

###Esentially all the docs defining the overall concept of Binary Tree shall will be here. For specific language implementation please refer to that languages forlder.

#Done
...

#In Progress
* python

#Introduction

#####What is a Binary Tree?
we've all heard that the term binary tree refers to a data structure, but what is it and what does it do?

The Binary tree is a **data structure** (keyword) which allows us to store information in it and retrieve it using big-O complexities. In specific we always, a programmers, need a method to store information and the Binary Tree gives us a method of inserting data into the structure (see what I did there?) is O(log<sub>2</sub>(n)) where n is the number of **nodes** (keyword) in the tree.

####Ok, how does a Binary Tree work?
So, how does this fundemental data structure work?

The *binary search tree* (BST) works as follows:

The tree starts at a single entry point - the *root node*. And the root node has a left and right pointer to an additional two nodes. Now, each one of those nodes also has a left and right pointer to two more additional nodes (hence called binary). This pattern goes on forever (figuratively). 
![BST Representation](http://i.stack.imgur.com/9XeYs.png)

###Insert
