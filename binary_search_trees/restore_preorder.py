from binary_search_trees.node import Node


def preorder_traversal(tree):
    if tree is None:
        return []
    order = []
    stack = [tree]
    while stack:
        cur = stack.pop()
        order.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return order


def rebuild_tree(preorder):
    if len(preorder) == 0:
        return None

    root = Node(preorder[0])
    if len(preorder) == 1:
        return root
    i = 1
    while i < len(preorder) and preorder[i] <= root.val:
        i += 1
    root.left = rebuild_tree(preorder[1:i])
    root.right = rebuild_tree(preorder[i:])
    return root


def is_tree_equal(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.val == root2.val and is_tree_equal(root1.left, root2.left) \
            and is_tree_equal(root1.right, root2.right):
        return True
    return False


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)

    node4.left = node2
    node2.left = node1
    node2.right = node3
    node4.right = node6
    node6.left = node5
    node6.right = node7
    node7.right = node8
    node8.right = node9
    preorder = preorder_traversal(node4)
    new_root = rebuild_tree(preorder)
    print(is_tree_equal(node4, new_root))

