from trees.node import Node


def inorder_traversal(root, path):
    if root is None:
        return

    inorder_traversal(root.left, path)
    path.append(root.val)
    inorder_traversal(root.right, path)


def preorder_traversal(root, path):
    if root is None:
        return

    path.append(root.val)
    preorder_traversal(root.left, path)
    preorder_traversal(root.right, path)


def reconstruct_tree(inorder, preporder):
    if len(preporder) == 0:
        return None

    if len(preporder) == 1:
        return Node(inorder[0])

    root_val = preporder[0]
    inorder_root_index = 0
    while inorder[inorder_root_index] != preporder[0]:
        inorder_root_index += 1

    root = Node(root_val)
    root.left = reconstruct_tree(inorder[:inorder_root_index], preporder[1:inorder_root_index + 1])
    root.right = reconstruct_tree(inorder[inorder_root_index + 1:], preporder[inorder_root_index+1:])
    return root


def tree_equal(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.val != root2.val:
        return False

    return tree_equal(root1.left, root2.left) and tree_equal(root1.right, root2.right)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node4.left = node2
    node2.left = node1
    node2.right = node3
    node4.right = node6
    node6.left = node5
    node6.right = node7
    inorder = []
    preporder = []
    inorder_traversal(node4, inorder)
    preorder_traversal(node4, preporder)
    print(inorder)
    print(preporder)
    new_root = reconstruct_tree(inorder, preporder)
    print(tree_equal(node4, new_root))
