import lists.node


def merge(l1, l2):
    head = tail = lists.node.Node(-1)

    if l1 and l2:
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
    else:
        if l1 or l2:
            if l1:
                return l1
            if l2:
                return l2

    return head


if __name__ == "__main__":
    l11 = lists.node.Node(1)
    l13 = lists.node.Node(3)
    l15 = lists.node.Node(5)
    l17 = lists.node.Node(7)

    l22 = lists.node.Node(2)
    l24 = lists.node.Node(4)
    l26 = lists.node.Node(6)

    l11.next = l13
    l13.next = l15
    l15.next = l17

    l22.next = l24
    l24.next = l26
    head = merge(l11, l22)
    while head.next:
        head = head.next
        print(head.val)
