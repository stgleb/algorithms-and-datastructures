from trees.node import Node


def is_balanced_util(root):
    if root is None:
        return True, 0

    left_result, left_height = is_balanced_util(root.left)
    right_result, right_height = is_balanced_util(root.right)

    if not left_result or not right_result:
        return False, 0

    if abs(left_height - right_height) > 1:
        return False, 0

    return True, max(left_height, right_height) + 1


def is_balanced(root):
    result, _ = is_balanced_util(root)
    return result


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
    print(is_balanced(node4))
    # unbalance tree
    node8 = Node(8)
    node9 = Node(9)
    node7.right = node8
    node8.right = node9
    print(is_balanced(node4))
