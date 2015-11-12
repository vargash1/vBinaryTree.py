#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: vargash1
# @Date:   2015-11-05 12:00:19
# @Email:  vargash1@wit.edu
# @Name :  Vargas, Hector
# @Last Modified by:   vargash1
# @Last Modified time: 2015-11-12 03:36:11
class BinaryTreeNode:
    """A Binary Tree node class that is used for the nodes in our tree 
    Attributes:
        data   (str|int|float):  Data that node holds.
        lchild (BinaryTreeNode): Left child of node.
        rchild (BinaryTreeNode): Right child of node.
    """
    def __init__(self,value):
        """
        Args:
            value (str|int|float): Data that node will hold.
        """
        self.data = value
        self.lchild = None
        self.rchild = None

# Inserts a single node into the tree
def insert(root,node):
    """
    Args:
        root: Root node from where tree spans from 
        node: New node to be added appropriately to the tree 
    Returns:
        None
    """
    if root is None:
        root = node
    else:
        # left side of our tree
        if root.data > node.data:
            # leaf is now in place
            if root.lchild is None:
                root.lchild = node
            else:
                insert(root.lchild,node)
        # right side of our tree
        else:
            if root.rchild is None:
                # leaf is now in place
                root.rchild = node
            else:
                insert(root.rchild,node)

# Inserts a list of items into the tree
def insert_list(root,arr):
    """
    Args:
        root: Root node from where tree spans from 
        arr:  List of values to be inserted into the tree 
    Returns:
        -1 if invalid arr passsed, None otherwise.
    """
    if (len(arr) <= 0):
        return -1
    for elem in arr:
        insert(root,BinaryTreeNode(elem))

# Finds node with maximum value in the tree
def findmax(root):
    """
    Args:
        root: Root node from where tree spans from 
    Returns:
        Max node value
    """
    if (root is None) or (root.rchild is None):
        return root
    return getmax(root.rchild)

# Finds node with 2nd max value
def secondmax(root):
    """
    Args:
        root: Root node from where tree spans from 
    Returns:
        -1 if failure, 2nd max node value otherwise.
    """
    if root is None:
        return -1
    
    #our second max is to the left of max node 
    if (root.rchild is None) and (root.lchild):
        return getmax(root.lchild)

    if root.rchild:
        # check if rchild of node in front of us is last node 
        # if so it is the max; current node is the jackpot
        if (root.rchild.rchild is None) and (root.rchild.lchild is None):
            return root.data
        return secondmax(root.rchild)

# Returns the sum of all nodes in the tree
def sum_all(root):
    """
    Args:
        root: Root node from where tree spans from 
    Returns:
        Sum of all node values, 0 if failure.
    """
    if root is None:
        return 0
    return (root.data + 
            sum_all(root.lchild) + 
            sum_all(root.rchild))
# returns the sum of nodes in a given range
def sum_range(root,low,high,total=0):
    """
    Args:
        root: Root node from where tree spans from 
        low:  Lowest value to consider for our range 
        high: Highest value to consider for our range 
        total(Optional): Used to sum up our total, default value is 0. 
    Returns:
        Sum of nodes whose values fall within the given range
        0 otherwise
    """
    # Check for erranous args
    if (root is None) or (low > high):
        return 0
    # Add only if within given intervals
    if (low <= root.data) and (high >= root.data):
        total += root.data
    return (total + 
            sum_range(root.lchild,low,high) + 
            sum_range(root.rchild,low,high)) 

# Returns an array with tree node values 
# Using inorder transversal
def inorder(root,arr=[]):
    """
    Args:
        root: Root node from where tree spans from 
        arr(Optional): defaulted to an empty list
    Returns:
        Array of node values inorder.
    """
    if root: 
        inorder(root.lchild)
        arr.append(root.data)
        inorder(root.rchild)
        return arr

# Returns an array with tree node values 
# Using preorder transversal
def preorder(root,arr=[]):
    """
    Args:
        root: Root node from where tree spans from 
        arr(Optional): defaulted to an empty list
    Returns:
        Array of node values preorder.
    """
    if root:
        arr.append(root.data)
        preorder(root.lchild)
        preorder(root.rchild)
        return arr

# Returns an array with tree node values
# Using postorder transversal
def postorder(root,arr=[]):
    """
    Args:
        root: Root node from where tree spans from 
        arr(Optional): defaulted to an empty list
    Returns:
        Array of node values postorder.
    """
    if root:
        postorder(root.lchild)
        postorder(root.rchild)
        arr.append(root.data)
        return arr
