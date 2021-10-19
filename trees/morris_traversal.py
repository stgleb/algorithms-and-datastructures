from trees.node import Node


def morris_traversal(root):
    cur = root
    while cur:
        if cur.left is None:
            print(cur.val)
            cur = cur.right
        else:
            cur2 = cur.left
            while cur2.right != cur and cur2.right is not None:
                cur2 = cur2.right
            if cur2.right == cur:
                cur2.right = None
                print(cur.val)
                cur = cur.right
            else:
                cur2.right = cur
                cur = cur.left


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
    print(morris_traversal(node4))

