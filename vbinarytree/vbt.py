#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: vargash1
# @Date:   2015-11-05 12:00:19
# @Email:  vargash1@wit.edu
# @Name :  Vargas, Hector
# @Last modified by:   vargash1
# @Last modified time: Wednesday, August 17th 2016, 7:27:06 pm
import sys
LIST_T = type([])
DICT_T = type({})

class BinaryTreeNode(object):
    """Binary Tree node
    Args:
        value  (object):  Data that node holds.
        lchild   (Node):  Left child of node.
        rchild   (Node):  Right child of node.
    """
    def __init__(self, value):
        self.data = value
        self.lchild = None
        self.rchild = None

def insert(root, node):
    """Inserts a single node into the tree. Elements are inserted lexicographically.
    Args:
        root (BinaryTreeNode): Root node
        node (object): Node data to be inserted
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
                insert(root.lchild, node)
        # right side of our tree
        else:
            if root.rchild is None:
                # leaf is now in place
                root.rchild = node
            else:
                insert(root.rchild, node)

def insert_list(root, arg_list):
    """Inserts a list of items into the tree. Will create a new node for each
    element in the list. Elements are inserted lexicographically.
    Args:
        root (BinaryTreeNode): Root node
        arg_list (list): A list whose values will be inserted into the tree
    """
    if len(arg_list) < 1:
        sys.exit("Can't insert an empty list")
    for element in arg_list:
        insert(root, BinaryTreeNode(element))

def insert_dict(root, arg_dict):
    """Inserts the keys and values of a dictionary into the tree Will zip the
    key and the value for each element into a tuple, and then insert each tuple
    into the tree as a node. Elements are inserted lexicographically.
    Args:
        root (BinaryTreeNode): Root node from where tree spans from
        arg_dict       (dict): Dictionary to insert
    """
    if len(arg_dict) < 1:
        sys.exit("Can't insert an empty dict")
    insert_list(root, zip(arg_dict.keys(), arg_dict.values()))

def find_max(root):
    """Finds node with maximum value in the tree
    Args:
        root(BinaryTreeNode): Root node
    Returns:
        BinaryTreeNode: contains maximum value data
    """
    if (root is None) or (root.rchild is None):
        return root
    return find_max(root.rchild)

def second_max(root):
    """Finds node with 2nd max value
    Args:
        root(BinaryTreeNode): Root node
    Returns:
        BinaryTreeNode: 2nd max node value or -1 if empty tree.
    """
    if root is None:
        return -1

    #our second max is to the left of max node
    if (root.rchild is None) and (root.lchild):
        return find_max(root.lchild)

    if root.rchild:
        # check if rchild of node in front of us is last node
        # if so it is the max; current node is the jackpot
        if root.rchild.rchild is None and root.rchild.lchild is None:
            return root
        return second_max(root.rchild)

def sum_all(root):
    """Sums up all node values in the tree.
    This will fail if all node values are not numerical.
    Args:
        root(BinaryTreeNode): Root node
    Returns:
        int: Sum of all node values or 0 if empty tree.
    """
    if root is None:
        return 0
    return root.data + sum_all(root.lchild) + sum_all(root.rchild)

def sum_range(root, low, high):
    """Sums of the node values whose values are within inclusive range
    Args:
        root (BinaryTreeNode): Root node
        low  (int): Low value to use for our inclusive range
        high (int): High value to use for our inclusive range
    Returns:
        int: Sum of nodes whose values fall within range.
             Returns 0 if args passed are invalid
    """
    if root is None or low > high:
        return 0
    # Add only if within given intervals
    operand = root.data if low <= root.data and high >= root.data else 0
    return (operand +
        sum_range(root.lchild, low, high) + sum_range(root.rchild, low, high))

def inorder(root, target=None):
    """Will traversere the tree using inorder protocol.
    If you pass a dict for target:
        Key will represent the order in which the node was visited.
        I.E the first node visited will have 1 for it's key.
    If you pass a list for target:
        The node value is appended according to visited order.
    Args:
        root (BinaryTreeNode): Root node
        target:
            list: List to write to
                    - OR -
            dict: Dictioanry to write to
    """
    if root:
        inorder(root.lchild, target)
        save_node_value(root.data, target)
        inorder(root.rchild, target)

def preorder(root, target=None):
    """Will traversere the tree using preorder protocol.
    If you pass a dict for target:
        Key will represent the order in which the node was visited.
        I.E the first node visited will have 1 for it's key.
    If you pass a list for target:
        The node value is appended according to visiting order.

    Args:
        root (object): Root node
        target:
            list: List to write to
                    - OR -
            dict: Dictioanry to write to
    """
    if root:
        save_node_value(root.data, target)
        preorder(root.lchild)
        preorder(root.rchild)

def postorder(root, target=None):
    """Will traversere the tree using postorder protocol.
    If you pass a dict for target:
        Key will represent the order in which the node was visited.
        I.E the first node visited will have 1 for it's key.
    If you pass a list for target:
        The node value is appended according to visiting order.
    If target is not passed, will print to console only.
    Args:
        root (object): Root node
        target:
            list: List to write to
                    - OR -
            dict: Dictioanry to write to
    """
    if root:
        postorder(root.lchild)
        postorder(root.rchild)
        save_node_value(root.data, target)

def save_node_value(data, target):
    """Utility method to save node data during traversal.
    Better to do this than have this block in each type of traversal
    """
    if isinstance(target, LIST_T):
        target.append(data)
    elif isinstance(target, DICT_T):
        target.update({len(target)+1:data})
    elif target is None:
        print data
