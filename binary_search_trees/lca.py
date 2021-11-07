from binary_search_trees.node import Node


def lca(root, node1, node2):
    if node1.val > node2.val:
        node1, node2 = node2, node1
    while root:
        if root.val > node2.val:
            root = root.left
        elif root.val < node1.val:
            root = root.right
        else:
            break
    return root


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
    print(lca(node4, node3, node7).val)
