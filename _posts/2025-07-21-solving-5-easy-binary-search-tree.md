### preface
i have never code anything that uses trees.
so this will be intresting and hard.


### my mindset
start by understand how tree works alongside theier basic operations.
after getting the basic operations down i just assume that i should
be able to solve this as it claims to be 'easy'


### taking a look at trees basics
Terms: <br>
Node, Root, Edges, Child, Parent, Leaf.
I think they are self-explanatory of what they are in a tree
<br>
<br>
Q What is a binary tree ? specifically <br>
- each node have two children: left/rigth

```python
# a tree node has a value
# and two pointers that points to the left and right child
class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right= None
```

<br>
<br>
Traversing a tree
- Dfs: recurse out each node
- Bfs: level by level


---

### Problem 1
<pre>
Problem

given the root of a node of a binary tree
and two integers low and high

return the sum of all nodes
with value in the inclusive range [low, high]

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
</pre>

my solution
```python
class Solution(object):
    def rangeSumBST(self, rot, low, high):
        return
```



