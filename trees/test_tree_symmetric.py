from trees.node import Node


def is_symmetric_util(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    return is_symmetric_util(root1.left, root2.right) and \
           is_symmetric_util(root1.right, root2.left)


def is_symmetric(root):
    if root is None:
        return True

    return is_symmetric_util(root.left, root.right)


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
    print(is_symmetric(node4))


