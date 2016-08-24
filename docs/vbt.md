# vbt.py

## Depth-First Traversals
I designed the preorder, inorder, and postorder traversals to provide more utility. Below you have a table of all implemented traversals in vbt.py, what should strike out to you is the argument `target`. It will default to `None`,  if you don't pass any value to it , the traversal will simply print out to stdout.

### Passing an empty list
If you pass an empty list, the traversal will not print to stdout. Instead it will write the traversed values to the list, in the order that they were traversed.

### Passing an empty dictionary
If you pass an empty dictionary, the traversal will not print to stdout. Instead it will write the traversed values to the dictionary. The keys to this dictionary are integers representing the order in which the node's value was visited. Let's say we visited a node with value 600 first, and then a node with value 300, and lastly a node with value 100.
Your dictionary will look like this:
```python
{
    1: 600, 2: 300, 3:100
}
```
### Examples
First declare the data structures prior to calling any methods.

** Please be aware that if the list you pass has the traversal values appended. If you pass a list that already contains values, they will still be in the list! **

** Please be aware that if the dictionary you pass has values in it, the key value pair may be overwritten, or the key value pair will remain in the dictionary.**

```python
empty_dict = {}
empty_list = []
```
| Traversal | Print to console | Save to list | Save to dict |
| :-------: | :--------------: | :----------: | :----------: |
| In-Order | `inorder(root)` | `inorder(root, target=empty_list)` | `inorder(root, target=empty_dict)` |
| Pre-Order | `preorder(root)` | `preorder(root, target=empty_list)` | `preorder(root, target=empty_dict)` |
| Post-Order | `postorder(root)` | `postorder(root, target=empty_list)` | `postorder(root, target=empty_dict)` |

```python
# In script or python shell
from vbinarytree import vbt

target_list = []
target_dict = {}

# Start with a root node
root = vbt.BinaryTreeNode(7)

# Insert elements using a list
vbt.insert_list(root,[1,0,3,2,5,4,6,9,8,10])

vbt.inorder(root)
# prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

vbt.inorder(root, target=target_list)
# target_list now contains:
target_list = [
    0, 1, 2, 3, 4,
    5, 6, 7, 8, 9, 10
]

vbt.inorder(root, target=target_dict)
# target_dict now contains:
target_dict = {
    1:0, 2:1, 3:2, 4:3, 5:4,
    6:5, 7:6, 8:7, 9:8, 10:9, 11:10
}
```
