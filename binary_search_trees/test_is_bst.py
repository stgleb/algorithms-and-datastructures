from binary_search_trees.node import Node


def is_bst_util(tree):
    if tree is None:
        return True, float('inf'), float('-inf')

    if tree.left:
        result_left, left_max, left_min = is_bst_util(tree.left)
    else:
        result_left, left_max, left_min = True, tree.val, tree.val

    if tree.right:
        result_right, right_max, right_min = is_bst_util(tree.right)
    else:
        result_right, right_max, right_min = True, tree.val, tree.val

    if not result_left or not result_right:
        return False, -1, -1

    if tree.val < left_max or tree.val > right_min:
        return False, -1, -1

    return True, right_max, left_min


def is_bst(tree):
    result, _, _ = is_bst_util(tree)
    return result


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
    print(is_bst(node4))
    print(is_bst(None))
