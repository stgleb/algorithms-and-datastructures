from trees.node import Node


def tree_exterior(root):
    stack = [(root, 0)]
    left_side = dict()
    right_side = dict()
    while len(stack) > 0:
        cur, level = stack.pop()
        if cur is None:
            continue
        if level not in left_side:
            left_side[level] = cur.val
        right_side[level] = cur.val
        stack.append((cur.right, level + 1))
        stack.append((cur.left, level + 1))

    return left_side.values(), right_side.values()


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
    node5.left = node8
    node8.right = node9
    print(tree_exterior(node4))
