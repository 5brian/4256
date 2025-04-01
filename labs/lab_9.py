class Node:
    def __init__(self, value, left_child=None, right_child=None):
        self.val = value
        self.left = left_child
        self.right = right_child

    def __str__(self):
        return str(self.val)


def is_full(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return is_full(root.left) and is_full(root.right)

    return False


def num_nodes(root):
    if root is None:
        return 0

    return 1 + num_nodes(root.left) + num_nodes(root.right)


def num_leaves(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return num_leaves(root.left) + num_leaves(root.right)


def height(root):
    if root is None:
        return -1

    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1


def is_perfect(root):
    h = height(root)
    n = num_nodes(root)

    return n == (2 ** (h + 1)) - 1


def has_value_bst(root, val):
    if root is None:
        return False
    if root.val == val:
        return True

    if val < root.val:
        return has_value_bst(root.left, val)

    return has_value_bst(root.right, val)
