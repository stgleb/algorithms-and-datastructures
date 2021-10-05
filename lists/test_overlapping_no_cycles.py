from lists.node import Node


def list_len(head):
    count = 0
    while head:
        head = head.next
        count += 1

    return count


def test_overlap(head1, head2):
    if head1 is None or head2 is None:
        return False

    while head1.next:
        head1 = head1.next

    while head2.next:
        head2 = head2.next

    if head1 is head2:
        return True

    return False


def find_overlapping_point(head1, head2):
    if not test_overlap(head1, head2):
        return None

    len1 = list_len(head1)
    len2 = list_len(head2)

    if len1 > len2:
        while len1 > len2:
            head1 = head1.next
            len1 -= 1
    elif len2 > len1:
        while len2 > len1:
            head2 = head2.next
            len2 -= 1

    while head1 is not head2:
        head1 = head1.next
        head2 = head2.next

    return head1.val


if __name__ == "__main__":
    l11 = Node(1)
    l13 = Node(3)
    l15 = Node(5)
    l17 = Node(7)

    l22 = Node(2)
    l24 = Node(4)
    l26 = Node(6)

    l11.next = l13
    l13.next = l15
    l15.next = l17

    l22.next = l24
    l24.next = l26
    l26.next = l15

    print(test_overlap(l11, l22))
    print(find_overlapping_point(l11, l22))
