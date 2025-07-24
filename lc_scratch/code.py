class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.left.right.left = TreeNode(6)
node.right.right = TreeNode(7)
wewant = """
we want:
| Postorder     | 4, 6, 5, 2, 7, 3, 1 |
| Inorder       | 4, 2, 6, 5, 1, 3, 7 |
| Preorder      | 1, 2, 4, 5, 6, 3, 7 |
    """


def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.value)
    inorder(node.right)

def preorder(node):
    return


def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.value)
    return


print(wewant)
postorder(node)
