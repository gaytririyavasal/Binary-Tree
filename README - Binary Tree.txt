
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

In this assignment, you will be adding to the classes Node and Tree that we developed in Binary Search Tree
Lecture and testing them. There are several short methods that you will have to write.

• Write a method range() that returns the range of values stored in a binary search tree of integers. The
range of values equals the maximum value in the binary search tree minus the minimum value. If
there is one value in the tree the range is 0. If the tree is empty the range is undefined.

def range (self):

• Write a method get level() that takes as input the level and returns a list of all the nodes at that level
from left to right. If that level does not exist for that binary search tree return an empty list . Use the
convention that the root is at level 0.

def get_level (self, level):

• Write a method left side view() when given the root of a binary tree, imagine yourself standing on the
left side of it, return the values of the nodes you can see ordered from top to bottom.

def left_side_view (self):

• Write a method sum leaf nodes() that returns the sum of the value of all leaves. Recall that a leaf node
does not have any children.

def sum_leaf_node (self):

In this assignment, you will be writing helper methods for the Tree class that we developed and test them.
The following is the outline of the code that you will be submitting. You may include the other functions
that we developed for completeness.

Input:

In the class TestBinaryTree, you will create several trees and show convincingly that your methods are
working. Here is an example of the file bst.in:

50 30 70 10 40 60 80 7 25 38 47 58 65 77 96
50 30 70 10 40 60 80 7 25 38 47 58 65 77 96
58 77 65 30 38 50 7 25 47 96 80 10 60 70 40
