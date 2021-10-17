class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def lca(node1, node2):
    first, second = node1, node2
    depth_first, depth_second = 0, 0
    while first:
        first = first.parent
        depth_first += 1
    while second:
        second = second.parent
        depth_second += 1

    first, second = node1, node2
    if depth_first > depth_second:
        while depth_first > depth_second:
            depth_first -= 1
            first = first.parent
    else:
        while depth_second > depth_first:
            depth_second -= 1
            second = second.parent

    while first and second and first is not second:
        first = first.parent
        second = second.parent

    return first


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
    node1.parent = node2
    node3.parent = node2
    node2.right = node3
    node2.parent = node4
    node4.right = node6
    node6.parent = node4
    node6.left = node5
    node6.right = node7
    node5.parent = node6
    node7.parent = node6
    print(lca(node3, node1).val)
