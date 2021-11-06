from binary_search_trees.node import Node


def k_largest_util(tree, k, result):
    if len(result) >= k:
        return False
    if tree is None:
        return True
    if k_largest_util(tree.right, k, result):
        result.append(tree.val)
        return k_largest_util(tree.left, k, result)
    return False


def k_largest(tree, k):
    result = []
    k_largest_util(tree, k, result)
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
    node7.right = node9
    print(k_largest(node4, 6))

