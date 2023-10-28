#!/usr/bin/env python3

#class that will be used to create node of the tree
class TreeNode:
    #this is the constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.l = None
        self.r = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.key < key:
            root.r = insert(root.r, key)
        else:
            root.l = insert(root.l, key)
    return root

def preorder_traversal(root):
    if root:
        print(root.key, end=" ")
        preorder_traversal(root.l)
        preorder_traversal(root.r)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.l)
        postorder_traversal(root.r)
        print(root.key, end=" ")

def main():
    print("Welcome to the Binary Search Tree.")
    
    data = list(map(int, input("Enter data to construct a BST: ").split()))
    root = None
    
    for item in data:
        root = insert(root, item)

    print("Pre-Order traversal of binary tree is:", end=" ")
    preorder_traversal(root)
    print()

    print("Post-Order traversal of binary tree is:", end=" ")
    postorder_traversal(root)
    print()

    choice = input("Do you want to try again? (Y/N): ").strip().lower()
    if choice != "n":
        main()
    else:
        print("Bye Bye!!")

if __name__ == "__main__":
    main()