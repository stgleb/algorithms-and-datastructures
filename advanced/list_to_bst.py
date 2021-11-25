class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.prev)
    print(root.val)
    inorder_traversal(root.next)


def convert_util(start, end):
    if start is None:
        return None
    if start is end:
        start.next = None
        start.prev = None
        return start

    slow, fast = start, start
    while fast != end:
        fast = fast.next
        slow = slow.next
        if not fast.next:
            break
        fast = fast.next
    root = slow
    root.prev = convert_util(start, root.prev)
    root.next = convert_util(root.next, end)
    return root


def convert_list_to_bst(head):
    start, end = head, head
    while end.next:
        end = end.next
    return convert_util(start, end)


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    n6.prev = n5
    n5.prev = n4
    n4.prev = n3
    n3.prev = n2
    n2.prev = n1

    root = convert_list_to_bst(n1)
    inorder_traversal(root)
