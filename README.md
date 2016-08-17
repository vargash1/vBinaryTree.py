#Binary Tree Implementation
This is a simple Implementation of a binary tree in python along with some useful methods. Feel free to take a look at mine and produce your own version. This project was intended to help anyone looking to implement a binary tree with ease. All of the included methods incorporate recursion.

###Included methods

| Method Name | Description                                         |
| :---------: | :-------------------------------------------------: |
| insert      | Inserts an element into the tree.                   |
| insert_list | Inserts a list into the tree.                       |
| insert_dict | Inserts a dict into the tree.                       |
| findmax     | Finds node whose data contains the maximum value.   |
| secondmax   | Finds node whose data contains the 2nd max value.   |
| sum_all     | Sums the node data from the entire tree.            |
| sum_range   | Sums the node data within passed inclusive range.   |
| inorder     | Traverse tree node values using inorder traversal.  |
| preorder    | Traverse tree node values using preorder traversal. |
| postorder   | Traverse tree node values using postorder traversal.|

###Install
```bash
    git clone git@github.com:vargash1/vBinaryTree.py.git
    # Ideally
    python setup.py install --home=~
    # Otherwise
    sudo python setup.py install
```
###Sample Usage
```python
	# In script or python shell
    from vbinarytree import vbt

    # Start with a root node
    root = vbt.BinaryTreeNode(7)

    # Insert elements using a list
    vbt.insert_list(root,[1,0,3,2,5,4,6,9,8,10])
    # vbt.insert_list(root, [x for x in xrange(10)])

    # Tranversals
    vbt.inorder(root)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    vbt.preorder(root)
    # [7, 1, 0, 3, 2, 5, 4, 6, 9, 8, 10]

    vbt.postorder(root)
    # [0, 2, 4, 6, 5, 3, 1, 8, 10, 9, 7]

    # Utility methods
    vbt.find_max(root).data
    # 10

    vbt.second_max(root).data
    # 9

    vbt.sum_all(root)
    # 55

    vbt.sum_range(root, low=0, high=5)
    # 15

    vbt.sum_range(root, low=0, high=1)
    # 1

    vbt.sum_range(root, low=20, high=565)
    # 0
```
