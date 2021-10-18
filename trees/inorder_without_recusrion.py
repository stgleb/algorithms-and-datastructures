from trees.node import Node


def inorder_traversal(root):
    if root is None:
        return

    stack = [root]
    while len(stack) > 0:
        cur = stack.pop()
        print(cur.val)
        if cur.right is not None:
            stack.append(cur.right)
        if cur.left is not None:
            stack.append(cur.left)


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
    inorder_traversal(node4)
