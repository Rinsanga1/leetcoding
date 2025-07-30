# Recursive traversal is pretty simple
but same can not be said for the iteration.

inorder
-
for this one you basicaly do backtracking
- have stack and node
- while stack / node exist
    - while node exists
        - append to stack
        - go left
        - this loop will end after it walks leftmost node
    - after the while loop ends, the node will be None, and we will now Backtrack
    - set node to stack.pop
    - go right by node = node.right, this is how you perform backtracking

```python
def inorder(root_node):
    if root_node is None:
        return
    stack = []
    node_ptr = root_node
    while node_ptr or stack:
        while node_ptr:
            stack.append(node_ptr)
            node_ptr = node_ptr.left
        node_ptr = stack.pop()
        print(node_ptr.value)
        node_ptr = node_ptr.right
    return
```

preorder
-
for this one, you just do what i call a stack and popping.
- start with a stack that have a root node
    - perform a loop with
    - pop the node
    - followed by appending the right and left node of said node
    - repeat. thats it.

this is a simple way of traversing, if all you need to do is traverse each node.
```python
def preorder(root_node):
    if root_node is None:
        return
    stack = [root_node]
    while stack:
        node_ptr = stack.pop()
        print(node_ptr.value)
        if node_ptr.right:
            stack.append(node_ptr.right)
        if node_ptr.left:
            stack.append(node_ptr.left)
    return

```

postorder
-
if you know how to perform preorder traversal you know how to do postorder.
- perform preorder
- append each value to a different stack 'stack2'as you traverse
- just pop the 'stack2'

Since, postorder is just the reverse of preorder.
you performa a preorder traversal and just reverse that.

```python
def postorder(root_node):
    if root_node is None:
        return
    stack1 = [root_node]
    stack2 = []
    while stack1:
        node_ptr = stack1.pop()
        stack2.append(node_ptr.value)
        if node_ptr.left:
            stack1.append(node_ptr.left)
        if node_ptr.right:
            stack1.append(node_ptr.right)
    while stack2:
        print(stack2.pop())
    return
```


bfs
-
just use deque.
if you understand pre order traversal, its the same thing.

```python
def bfs(root_node):
    if root_node is None:
        return
    queue = deque([root_node])
    while queue:
        node_ptr = queue.popleft()
        print(node_ptr.value)
        if node_ptr.left:
            queue.append(node_ptr.left)
        if node_ptr.right:
            queue.append(node_ptr.right)
    return

```
