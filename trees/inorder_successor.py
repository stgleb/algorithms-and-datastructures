class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def inorder_successor(node):
    if node is None:
        return None
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    while node.parent and node == node.parent.right:
        node = node.parent
    return node.parent


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
    print(inorder_successor(node3).val)
