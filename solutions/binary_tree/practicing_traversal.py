# traversal practice for tree
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


Node = TreeNode(1)
Node.left = TreeNode(2)
Node.right = TreeNode(3)
Node.left.left = TreeNode(4)
Node.left.right = TreeNode(5)
Node.left.right.left = TreeNode(6)
Node.right.right = TreeNode(7)



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


print('inorder')
inorder(Node)

print('preorder')
preorder(Node)

print('postorder')
postorder(Node)

print('BFS')
bfs(Node)
