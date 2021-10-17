from trees.node import Node


def lca_util(root, node1, node2):
    if root is None:
        return 0, None

    status_left, lca_node = lca_util(root.left, node1, node2)
    if lca_node is not None:
        return status_left, lca_node
    status_right, lca_node = lca_util(root.right, node1, node2)
    if lca_node is not None:
        return status_right, lca_node

    status = status_left + status_right
    if status == 2:
        return status, root
    if (root is node1 or root is node2) and status + 1 == 2:
        return status + 1, root
    elif root is node1 or root is node2:
        return status + 1, None

    return status, None


def lca(root, node1, node2):
    _, lca_node = lca_util(root, node1, node2)
    return lca_node


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(3)
    node6 = Node(2)
    node7 = Node(1)

    node4.left = node2
    node2.left = node1
    node2.right = node3
    node4.right = node6
    node6.left = node5
    node6.right = node7
    print(lca(node4, node3, node2).val)
