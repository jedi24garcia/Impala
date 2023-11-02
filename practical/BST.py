#!/usr/bin/env python3

#class that will be used to create node of the tree
class TreeNode:
    #this is the constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.l = None
        self.r = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, root, key):
        if root is None:
            root = TreeNode(key)
        else:
            if root.key < key:
                root.r = self.insert(root.r, key)
            else:
                root.l = self.insert(root.l, key)
        return root

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
        tree.root = tree.insert(tree.root, item)

    print("Pre-Order traversal of binary tree is:", end=" ")
    preorder_traversal(tree.root)
    print()

    print("Post-Order traversal of binary tree is:", end=" ")
    postorder_traversal(tree.root)
    print()

    choice = input("Do you want to try again? (Y/N): ").strip().lower()
    if choice != "n":
        main()
    else:
        print("Bye Bye!!")

if __name__ == "__main__":
    main()