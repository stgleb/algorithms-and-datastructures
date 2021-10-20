class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


def connect_levels(root):
    def connect_level(cur_root):
        while cur_root:
            next_node = cur_root.next
            while next_node and next_node.left and next_node.right:
                next_node = next_node.next

            if cur_root.left and cur_root.right:
                cur_root.left.next = cur_root.right

                if next_node:
                    cur_root.right.next = next_node.right
                    if next_node.left:
                        cur_root.right.next = next_node.left
            elif cur_root.left and next_node:
                cur_root.left.next = next_node.right

                if next_node.left:
                    cur_root.left.next = next_node.left
            elif cur_root.right and next_node:
                cur_root.right.next = next_node.right

                if next_node.left:
                    cur_root.right.next = next_node.left
            cur_root = next_node

    while root:
        connect_level(root)
        if root.left:
            root = root.left
        else:
            root = root.right


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node4.left = node2
    # node2.left = node1
    node2.right = node3
    node4.right = node6
    # node6.left = node5
    node6.right = node7
    connect_levels(node4)
    root = node4
    while root:
        cur = root
        while cur:
            print(cur.val)
            cur = cur.next
        print("-------------------")
        if root.left:
            root = root.left
        else:
            root = root.right