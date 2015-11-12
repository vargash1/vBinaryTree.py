#Binary Tree Implementation
This is a simple Implementation of a binary tree in python along with some useful methods. Feel free to take a look at mine and produce your own version. This project was intended to help anyone looking to implement a binary tree with ease. All of the included methods incorporate recursion, after all we are working with a Binary Tree!

###Included methods
* insert -- inserts an element into the tree
* insert_list -- inserts an array/list into the tree
* findmax -- Finds node whose data contains the maximum value.
* secondmax -- Finds node whose data contains the 2nd max value.
* sum_all -- Sums the node data from the entire tree.
* sum_range -- Sums the node data that is within the given range from the enitre tree.
* inorder -- Returns an array with tree node values using inorder traversal.
* preorder -- Returns an array with tree node values using preorder traversal.
* postorder -- Returns an array with tree node values using postorder traversal.

###Install
```bash
	#in some dir
    git clone git@github.com:vargash1/vBinaryTree.py.git
    python setup.py install
```
###Sample Usage
```python
	#In script or python shell
	
    from vbinarytree import vbt
    
    #Start with a root node
    root = vbt.BinaryTreeNode(7)
    
    #Insert elements using a list
    vbt.insert_list(root,[1,0,3,2,5,4,6,9,8,10])
    
    #Tranversals
    vbt.inorder(root)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    vbt.preorder(root)
    # [7, 1, 0, 3, 2, 5, 4, 6, 9, 8, 10]

    vbt.postorder(root)
    # [0, 2, 4, 6, 5, 3, 1, 8, 10, 9, 7]

```