---
layout: post
title:  learning tree traversal
date:   2025-07-24 05:17:48 +0530
categories: jekyll update
---


# Recursive Traversal Is Pretty Simple
_But the same cannot be said for the iterative approach._

---

## Inorder Traversal

For this one, you basically do **backtracking**:

- Use a stack and a node pointer.
- While the stack or the current node exists:
  - While the node exists:
    - Append it to the stack.
    - Go left.
    - This loop ends after reaching the leftmost node.
  - After the inner loop ends, the node will be `None`, so now we backtrack:
    - Set the node to `stack.pop()`.
    - Go right by setting `node = node.right`.
      This is how you perform backtracking.

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

---

## Preorder Traversal

For this one, you just do what I call **stack and popping**:

- Start with a stack containing the root node.
- Perform a loop:
  - Pop the node.
  - Print or process the node’s value.
  - Append the right child first, then the left child (if they exist).
- Repeat until the stack is empty.

This is a simple way of traversing if all you need to do is visit each node.

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

---

## Postorder Traversal

If you know how to perform preorder traversal, you already know how to do postorder.

- Perform a preorder traversal.
- Instead of printing immediately, append each node’s value to a second stack, `stack2`.
- After traversal, pop and print values from `stack2`.

Since postorder is just the **reverse** of preorder, this works nicely.

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

---

## Breadth-First Search (BFS)

Just use a `deque` (double-ended queue). If you understand preorder traversal, BFS is similar conceptually but uses a queue instead of a stack:

```python
from collections import deque

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

---
