#!/usr/bin/env python3

# Creating a constructor. The class TreeNode represents a node in the Binary Search Tree
class TreeNode:
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
            return TreeNode(key)
        if key < root.key: # if key is less than root.key, it simply means the new node must be placed in the left subtree.
            root.r = self._insert_recursive(root.r, key)
        elif key > root.key: # if key is greater than root.key, it simply means the new node must be placed in the right subtree.
            root.l = self._insert_recursive(root.l, key)
        return root # returns the current 'root' code

def preorder_traversal(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            print(node.key, end=" ")
            stack.append(node.r)
            stack.append(node.l)

def postorder_traversal(root):
    stack = [root]
    outcome = []
    while stack:
        node = stack.pop()
        if node:
            outcome.append(node.key)
            stack.append(node.l)
            stack.append(node.r)
    while outcome:
        print(outcome.pop(), end=" ")

def main():
    print("Welcome to the Binary Search Tree.")
    
    data = list(map(int, input("Enter data to construct a BST: ").split()))
    tree = BinarySearchTree()

    for item in data:
        tree.insert(item)

    print("Pre-Order traversal of binary tree is:", end=" ")
    preorder_traversal(tree.root)
    print()

    print("Post-Order traversal of binary tree is:", end=" ")
    postorder_traversal(tree.root)
    print()

    UserOption = input("Do you want to try again? (Y/N): ").strip().lower()
    if UserOption != "n":
        main()
    else:
        print("Bye Bye!!")

if __name__ == "__main__":
    main()