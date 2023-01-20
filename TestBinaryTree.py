#  File: TestBinaryTree.py

#  Description: The following program adds to the classes Node and Tree as developed in class.

#  Student Name: Gaytri Riya Vasal

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/7/2022

#  Date Last Modified: 7/10/2022

import sys

class Node (object):
    
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1

class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def __set_root__(root):
        self.root = root

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    # Returns the node with the smallest value in the tree
    def minimum(self):
        
        current = self.root # Initalize current at self.root
        parent = current # Set parent equal to current
        
        while (current != None): # Continue while loop until current is None
            
            parent = current # Set parent equal to current
            current = current.lChild # Set the value of current to the left child
            
        return parent

    # Returns the node with the largest value in the tree
    def maximum(self):
        
        current = self.root # Initalize current at self.root
        parent = current # Set parent equal to current
        
        while (current != None): # Continue while loop until current is None
            
            parent = current # Set parent equal to current
            current = current.rChild # Set the value of current to the right child
            
        return parent

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        
        if self.root ==  None: # If there is no root, return None
            return None
        
        elif self.root.lChild == None and self.root.rChild == None: # Consider the case of a leaf node
            return 0
        
        else: # Otherwise, return the difference between the maximum and minimum value of the tree
            return self.maximum().data - self.minimum().data

    # Enables a pre order traversal of the tree
    def preorder(self, root, level, d):
 
        if root is None: # If the tree is empty, simply return
            return
 
        d.setdefault(level, []).append(root) # Insert the current node as well as its level into the dictionary
 
        self.preorder(root.lChild, level + 1, d) # Recur for the left subtree by increasing the level by 1
        self.preorder(root.rChild, level + 1, d) # Recur for the right subtree by increasing the level by 1
    
    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):

        d = {} # Create an empty dictionary to store nodes between given levels
 
        self.preorder(self.root, 0, d) # Traverse the tree and insert its nodes into the dictionary in correspondence to their levels

        if len(d) < level + 1: # If the length of the dictionary is less than level + 1, return an empty list
            return []
 
        return d.get(level) if self.root != None else [] # If the root is not None, return d.get(level); if the root is None, return an empty list

    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):

        d = {} # Create an empty dictionary to store nodes between given levels
 
        self.preorder(self.root, 0, d) # Traverse the tree and insert its nodes into the dictionary in correspondence to their levels

        lst = [] # Instantiate empty list
        
        for key in d: # Traverse keys of dictionary
            lst.append(d[key][0].data) # Append the data of the leftmost element to the list

        return lst # Return the list with all left elements appended

    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):

        if (self.root == None): # If there is no root, simply return
            return

        summation = 0 # Initialize summation variable at 0

        d = {} # Instantiate dictionary

        self.preorder(self.root, 1, d) # Call the preorder method with self.root, 1, and d as inputs

        for key in d: # Traverse keys in dictionary
            for element in d[key]: # Traverse each element in d[key]
                if element.lChild == None and element.rChild == None: # In the case of a leaf node, add the element's data to the sum
                    summation += element.data

        return summation # Return the final summation

def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree

# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescope will import your classes and call the methods.

# Test on Unbalanced Tree | The functionality of each method has been tested and matches the expected results
# after creating the binary search tree on the class visualization tool.

data = [40, 80, 90, 10, 100, 50, 40, 80, 40, 20, 15, 60]
unbalancedtree = make_tree(data)

print(unbalancedtree.range())
print(unbalancedtree.get_level(0))
print(unbalancedtree.get_level(1))
print(unbalancedtree.get_level(2))
print(unbalancedtree.get_level(3))
print(unbalancedtree.get_level(4))
print(unbalancedtree.get_level(5))
print(unbalancedtree.left_side_view())
print(unbalancedtree.sum_leaf_nodes())

# Test on Balanced Tree | The functionality of each method has been tested and matches the expected results
# after creating the binary search tree on the class visualization tool.

data = [30, 17, 11, 19, 37, 31, 38]
balancedtree = make_tree(data)

print(balancedtree.range())
print(balancedtree.get_level(0))
print(balancedtree.get_level(1))
print(balancedtree.get_level(2))
print(balancedtree.get_level(3))
print(balancedtree.left_side_view())
print(balancedtree.sum_leaf_nodes())

# Test on Empty Tree | The functionality of each method has been tested and matches the expected results
# after creating the binary search tree on the class visualization tool.

data = []
emptytree = make_tree(data)

print(emptytree.range())
print(emptytree.get_level(0))
print(emptytree.left_side_view())
print(emptytree.sum_leaf_nodes())

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

    # Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")
    
    # Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")

if __name__ == "__main__":
    main()
