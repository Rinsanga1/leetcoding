class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_inorder_iterative(root: TreeNode):
    stack = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.value)
        current = current.right


# binary tree
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.left = TreeNode(6)
node.right.right = TreeNode(7)

print("Iterative In-order Traversal:")
tree_inorder_iterative(node)
