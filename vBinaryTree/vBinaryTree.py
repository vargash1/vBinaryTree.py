#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: vargash1
# @Date:   2015-11-05 12:00:19
# @Email:  vargash1@wit.edu
# @Name :  Vargas, Hector
# @Last Modified by:   vargash1
# @Last Modified time: 2015-11-11 02:04:38
class BinaryTreeNode:
    def __init__(self,value):
        self.data = value
        self.lchild = None
        self.rchild = None
# inserts an element into the tree
def insert(root,node):
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

def getmax(root):
    if (root is None) or (root.rchild is None):
        return root
    return getmax(root.rchild)

def secondmax(root):
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

def find_sum_range(range,total = 0):
	
	return total

# Returns an array with tree nodes in inorder
def inorder(root,arr=[]):
    if root:
        inorder(root.lchild)
        arr.append(root.data)
        inorder(root.rchild)
        return arr

# Returns an array with tree nodes in preorder
def preorder(root,arr=[]):
    if root:
        arr.append(root.data)
        preorder(root.lchild)
        preorder(root.rchild)
        return arr

# Returns an array with tree nodes in postorder
def postorder(root,arr=[]):
    if root:
        postorder(root.lchild)
        postorder(root.rchild)
        arr.append(root.data)
        return arr

# Cleaner than calling in main method
def main():
    origin = BinaryTreeNode(7)
    tmp_arr = [1,0,3,2,5,4,6,9,8,10]
    for elem in tmp_arr:
        insert(origin,BinaryTreeNode(elem))
main()