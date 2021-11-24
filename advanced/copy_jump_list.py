class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.jump = None


def copy_jump_list(head):
    old_head = head
    new_head = None
    while head:
        next = head.next
        new_node = Node(head.val)
        new_node.next = next
        head.next = new_node
        if not new_head:
            new_head = new_node
        head = next

    cur = old_head
    while cur and cur.next:
        cur.next.jump = cur.jump
        cur = cur.next.next
    return new_head


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

    n1.jump = n3
    n2.jump = n4
    n3.jump = n5
    n4.jump = n6
    n5.jump = n2
    head2 = copy_jump_list(n1)
    head = n1

    while head:
        print(head.val)
        head = head.jump

    print("-----------------")
    while head2:
        print(head2.val)
        head2 = head2.jump
