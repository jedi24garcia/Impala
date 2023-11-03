#!/usr/bin/env python3

# Creating a constructor. The class TreeNode represents a node in the Binary Search Tree
class Node:
    # constructor method for class TreeNode. The key parameter initializes a new node whereas left (l) and right (r) are set to default which is 'None'.
    def __init__(self, key=None):
        self.key = key
        self.l = None
        self.r = None

class BinarySearchTree:
    # constructor method for class BinarySearchTree. 
    def __init__(self):
        self.root = None

    def insert(self, stats):
        self.root = self._insert_recursive(self.root, stats) # this method is to insert the key into the tree
    
    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key: # if key is less than root.key, it simply means the new node must be placed in the left subtree
            root.r = self._insert_recursive(root.r, key)
        elif key > root.key: # if key is greater than root.key, it simply means the new node must be placed in the right subtree
            root.l = self._insert_recursive(root.l, key)
        return root # returns the current 'root' code

def preorder_traversal(root):
    pre_stack = [root] # initializes stack with the root to commence pre-order traversal
    while pre_stack: # loops
        node = pre_stack.pop() # represents the node to be processed for pre-order traversal
        if node:
            print(node.key, end=" ") # this prints the key of the current node for the pre-order part, where the root is visited first
            pre_stack.append(node.r) # pushes right child of the node onto the stack and ensures right subtree will be visited after left subtree
            pre_stack.append(node.l) # vice-versa to stack.append(node.r) for pre-order traversal

def postorder_traversal(root):
    post_stack = [root] # initializes stack with the root to commence post-order traversal
    outcome = [] # this creates an empty list 'outcomes' to help store the keys in correct order 
    while post_stack: # loops
        node = post_stack.pop() # represents the node to be processed for post-order traversal
        if node:
            outcome.append(node.key) # this appends the key of the current node to the empty list 'outcome'.
            post_stack.append(node.l) # pushes right child of the node onto the stack and ensures right subtree will be visited after left subtree
            post_stack.append(node.r) # vice-versa to stack.append(node.r) for post-order traversal
    while outcome:
        print(outcome.pop(), end=" ") # when all nodes are processed completely, the keys stored
        # in the outcome list are printed in a reversal order to accomplish post-order traversal

# The whole function below is responsible for the running the whole program as this takes
# the users input to create a BST and carry out pre-order and post traversals as defined.
def main():
    print("Welcome to the Binary Search Tree.")
    
    # prompts users to enter a list. This also splits the into list of integers using split()
    datas = [int(item) for item in input("Enter data to construct a BST: ").split()]
    BSTtree = BinarySearchTree()

    # loops
    for item in datas:
        BSTtree.insert(item)

    print("Pre-Order traversal of binary tree is:", end=" ")
    preorder_traversal(BSTtree.root)

    print("\nPost-Order traversal of binary tree is:", end=" ")
    postorder_traversal(BSTtree.root)
    print()
    
    # If the users want to try to run the program again, this component calls itself recursively.
    UserOption = input("Do you want to try again? (Y/N): ").strip().lower()
    if UserOption != "n":
        main()
    else:
        print("Bye Bye!!")

if __name__ == "__main__":
    main()

# ANALYSIS
# 1. Why did you select that specific data structure? 
# This structure allows me or the users to enter data to construct a BST in which it traverse
# the tree in pre-order and post-order, respectively. I have chosen NODE data structure to
# implement BST as it is a natural pick for representing a BST. I have documented each line for a better understanding.
# 2. How was that data structure suited to the task?
# The data structure suited the task as running the program performs as its intructed. It shows
# no error or bug and runs similar to the output of the task. The Node data structure
# is a natural fit for executing BST because of its alignment with higher structure as well as
# its effieciency in carrying out BST operations.
# 3. Could another data structure be used to complete the same task? If so, how would your solution differ?
# Yes, absolutely. There are other ways of data structure that can done to complete this task.
# For example, you can define a delete operation if you are looking for a more complex solutions and also, 
# a recursive function that allows you to return the new state of the given node after carrying out
# the delete operation. Another method would be to create an exists function. This is another
# recursive function that would return 'True' or 'False' depending on wether a specified value
# that exists already in the tree.