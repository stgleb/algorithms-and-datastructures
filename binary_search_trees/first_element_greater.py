from binary_search_trees.node import Node


def first_element_greater(tree, value):
    if tree is None:
        return None

    element = tree
    while tree:
        if tree.val < value:
            tree = tree.right
        else:
            element = tree
            tree = tree.left
    return element.val


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
    print(first_element_greater(node4, 8))

