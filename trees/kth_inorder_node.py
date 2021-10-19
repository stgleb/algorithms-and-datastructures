class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.count = 1


def kth_node(root, k):
    if root is None:
        return None

    left_count = root.left.count if root.left else 0
    if left_count + 1 == k:
        return root
    elif left_count + 1 > k:
        return kth_node(root.left, k)
    else:
        return kth_node(root.right, k - left_count - 1)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node4.left = node2
    node4.count = 7
    node2.count = 3
    node6.count = 3
    node2.left = node1
    node2.right = node3
    node4.right = node6
    node6.left = node5
    node6.right = node7
    print(kth_node(node4, 6).val)


