from binary_search_trees.node import Node


def build_min_height_bst(arr):
    if len(arr) == 0:
        return None

    if len(arr) == 1:
        return Node(arr[0])

    m = len(arr) // 2
    root = Node(arr[m])
    root.left = build_min_height_bst(arr[:m])
    root.right = build_min_height_bst(arr[m + 1:])
    return root


def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val)
    inorder_traversal(root.right)


if __name__ == "__main__":
    tree = build_min_height_bst([1, 2, 3, 4, 5, 6, 7])
    inorder_traversal(tree)

