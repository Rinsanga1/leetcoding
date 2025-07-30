# Binary Tree Practice Roadmap

This roadmap is designed to help you learn and master binary tree operations,
starting from the absolute basics and gradually moving towards more complex
problems often found on platforms like LeetCode. Focus on understanding the
underlying concepts and different traversal methods.

---

##

Before diving into binary trees, let's ensure we have a solid understanding
of the foundational concepts.

### 0.1 What is a Data Structure?
*   **Concept:** Understand that a data structure is a way of organizing and
    storing data in a computer so that it can be accessed and modified
    efficiently. Trees are a specific type of non-linear data structure.

### 0.2 Nodes and References/Pointers
*   **Concept:** In many data structures, especially trees and linked lists,
    data is stored in "nodes." These nodes are connected to each other using
    "references" (or "pointers" in some languages). A reference is
    essentially an address in memory that points to another node.
*   **Task:** Think about how you would represent a connection between two
    pieces of data in code.

### 0.3 Introduction to Recursion
*   **Concept:** Recursion is a powerful programming technique where a function
    calls itself to solve a problem. It's fundamental to understanding and
    implementing many tree algorithms.
    *   **Base Case:** A condition that stops the recursion. Without it, the
        function would call itself indefinitely.
    *   **Recursive Step:** The part where the function calls itself, usually
        on a smaller subproblem.
*   **Example:** Let's consider a simple recursive function to calculate the
    factorial of a number `n` (n! = n * (n-1)!):
    ```python
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive step
        return n * factorial(n - 1)
    ```
*   **Task:** Implement the `factorial` function yourself. Trace its
    execution for `factorial(3)`. Understand how the call stack works.

---

##

At this stage, the goal is to grasp what a binary tree is, how nodes are
structured, and the fundamental ways to navigate through them.

### 1.0 Defining a `TreeNode` Class
*   **Concept:** A binary tree node is the fundamental building block. Each
    node typically holds a value and references to its left and right children.
*   **Task:** Create a simple class for a binary tree node. It should have:
    *   `val`: The value stored in the node (e.g., an integer).
    *   `left`: A reference to the left child node. Initialize to `None` (or
        `null`) if no child exists.
    *   `right`: A reference to the right child node. Initialize to `None` (or
        `null`) if no child exists.
*   **Example (Python):**
    ```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    ```

### 2.0 Building Your First Trees
*   **Concept:** Trees are formed by linking `TreeNode` objects together.
*   **Task:
    *   Create a simple 3-node tree manually:
        ```
              1
             / \
            2   3
        ```
        (i.e., `root = TreeNode(1)`, `root.left = TreeNode(2)`,
        `root.right = TreeNode(3)`)
    *   Create a slightly larger tree manually (e.g., a complete binary tree
        of depth 2, which has 7 nodes).

### 3.0 Tree Traversal - Inorder (Recursive)
*   **Concept:** Inorder traversal visits nodes in the order: Left subtree ->
    Root -> Right subtree. For a Binary Search Tree (which we'll cover later),
    this traversal visits nodes in ascending order of their values. Recursion
    is very natural for this.
*   **Task:** Implement a recursive function `inorder_traversal(root)` that
    prints the values of the nodes in inorder.
*   **Goal:** Understand how recursion naturally handles tree structures.
*   **Trace:** Trace the execution of your `inorder_traversal` function on the
    3-node tree you created.

### 4.0 Tree Traversal - Inorder (Iterative)
*   **Concept:** While recursion is elegant, it can lead to stack overflow for
    very deep trees. Iterative solutions use an explicit stack data structure
    to simulate the recursion.
*   **Task:** Implement an iterative function `inorder_traversal_iterative(root)`
    that prints the values of the nodes in inorder using a stack.
*   **Goal:** Understand how a stack can simulate recursion and manage the
    traversal state.
*   **Trace:** Trace the execution of your iterative function on a small tree.

### 5.0 Tree Traversal - Preorder (Recursive & Iterative)
*   **Concept:** Preorder traversal visits nodes in the order: Root -> Left
    subtree -> Right subtree. It's often used to create a copy of a tree.
*   **Task:** Implement both recursive and iterative `preorder_traversal(root)`
    functions.
*   **Goal:** Understand its use cases (e.g., creating a copy of a tree).

### 6.0 Tree Traversal - Postorder (Recursive & Iterative)
*   **Concept:** Postorder traversal visits nodes in the order: Left subtree ->
    Right subtree -> Root. It's often used for deleting a tree (deleting
    children before the parent).
*   **Task:** Implement both recursive and iterative `postorder_traversal(root)`
    functions.
*   **Goal:** Understand its use cases (e.g., deleting a tree).

### 7.0 Tree Traversal - Level Order (Breadth-First Search - BFS)
*   **Concept:** Level order traversal visits nodes level by level, from left to
    right. It uses a queue data structure.
*   **Task:** Implement `level_order_traversal(root)` using a queue.
*   **Goal:** Understand how BFS explores nodes level by level, which is crucial
    for many tree problems where you need to process nodes at the same depth.

---

##

Now that you understand traversals, let's apply them to solve common,
straightforward tree problems. These problems will reinforce your
understanding of recursion and basic tree properties.

### 1.0 Find the Maximum Depth/Height of a Binary Tree
*   **Problem:** Given the root of a binary tree, return its maximum depth. The
    maximum depth is the number of nodes along the longest path from the root
    node down to the farthest leaf node.
*   **Hint:** This is a classic recursive problem. Think about the depth of a
    node in terms of the maximum depth of its children. The depth of a `None`
    node is 0.
*   **Task:** Implement `max_depth(root)`.

### 2.0 Invert/Flip a Binary Tree
*   **Problem:** Given the root of a binary tree, invert the tree, and return
    its root. Inverting means swapping the left and right children of every
    node.
*   **Hint:** This can be done recursively. For each node, swap its left and
    right children, then recursively invert its new left and right subtrees.
*   **Task:** Implement `invert_tree(root)`.

### 3.0 Check if Two Trees are the Same
*   **Problem:** Given the roots of two binary trees, `p` and `q`, return
    `true` if they are structurally identical and have the same node values,
    or `false` otherwise.
*   **Hint:** Compare nodes recursively. If both are `None`, they are the same.
    If one is `None` and the other is not, they are different. If their values
    are different, they are different. Otherwise, recursively check their left
    and right children.
*   **Task:** Implement `is_same_tree(p, q)`.

### 4.0 Symmetric Tree
*   **Problem:** Given the root of a binary tree, check whether it is a mirror
    of itself (i.e., symmetric around its center).
*   **Hint:** This is similar to checking if two trees are the same, but you're
    comparing a node's left subtree with its right subtree (mirrored). You'll
    need a helper function that compares two nodes, say `is_mirror(node1,
    node2)`, where `node1.left` is compared with `node2.right`, and
    `node1.right` with `node2.left`.
*   **Task:** Implement `is_symmetric(root)`.

### 5.0 Path Sum
*   **Problem:** Given the `root` of a binary tree and an integer `targetSum`,
    return `true` if the tree has a root-to-leaf path such that adding up all
    the values along the path equals `targetSum`. A leaf is a node with no
    children.
*   **Hint:** Use recursion. When you visit a node, subtract its value from
    `targetSum`. If you reach a leaf node and the remaining `targetSum` is 0,
    you've found a path.
*   **Task:** Implement `has_path_sum(root, targetSum)`.

---

##

These problems require a deeper understanding of tree properties, more complex
traversals, or combining multiple concepts.

### 1.0 Binary Tree Level Order Traversal II (Bottom-Up)
*   **Problem:** Given the root of a binary tree, return the bottom-up level
    order traversal of its nodes' values. (i.e., from leaf to root, level by
    level).
*   **Hint:** Perform a regular level order traversal (BFS), collect the
    results for each level, and then reverse the order of the levels.
*   **Task:** Implement `level_order_bottom(root)`.

### 2.0 Validate Binary Search Tree (BST)
*   **Problem:** Given the root of a binary tree, determine if it is a valid
    Binary Search Tree (BST).
    *   The left subtree of a node contains only nodes with values less than
        the node's value.
    *   The right subtree of a node contains only nodes with values greater
        than the node's value.
    *   Both the left and right subtrees must also be BSTs.
*   **Hint:** A common mistake is to only check immediate children. You need to
    ensure that *all* nodes in the left subtree are less than the current
    node, and *all* nodes in the right subtree are greater. This requires
    passing min/max bounds during recursion. For example, when traversing
    left, the current node's value becomes the new upper bound.
*   **Task:** Implement `is_valid_bst(root)`.

### 3.0 Lowest Common Ancestor of a Binary Tree
*   **Problem:** Given a binary tree, find the lowest common ancestor (LCA) of
    two given nodes `p` and `q`. The LCA is the lowest node in the tree that
    has both `p` and `q` as descendants (where we allow a node to be a
    descendant of itself).
*   **Hint:** Recursively search for `p` and `q`. If a node is `p` or `q`, or
    if `p` and `q` are found in its left and right subtrees respectively,
    then that node is the LCA.
*   **Task:** Implement `lowest_common_ancestor(root, p, q)`.

### 4.0 Construct Binary Tree from Preorder and Inorder Traversal
*   **Problem:** Given two integer arrays `preorder` and `inorder` where
    `preorder` is the preorder traversal of a binary tree and `inorder` is
    the inorder traversal of the same tree, construct and return the binary
    tree.
*   **Hint:** The first element of preorder is always the root. Inorder
    traversal helps identify the left and right subtrees: elements to the left
    of the root in inorder form the left subtree, and elements to the right
    form the right subtree. This problem is best solved recursively.
*   **Task:** Implement `build_tree(preorder, inorder)`.

### 5.0 Binary Tree Zigzag Level Order Traversal
*   **Problem:** Given the root of a binary tree, return the zigzag level order
    traversal of its nodes' values. (i.e., from left to right, then right to
    left for the next level and so on).
*   **Hint:** Use a deque (double-ended queue) or a flag to alternate between
    adding elements to the front or back of the current level's list during a
    BFS traversal.
*   **Task:** Implement `zigzag_level_order(root)`.

---

Good luck with your practice! Remember to draw out trees, trace your code, and
understand why each approach works.
