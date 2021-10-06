from lists.node import Node


def find_mid_point(head):
    list_len = 0
    cur = head
    while cur:
        cur = cur.next
        list_len += 1

    for _ in range(list_len // 2):
        head = head.next
    return head


def reverse(head):
    prev, cur, next = None, head, head.next
    while next:
        cur.next = prev
        prev = cur
        cur = next
        next = next.next
    cur.next = prev
    return cur


def is_palindromic(start, mid):
    while mid:
        if start.val != mid.val:
            return False
        start = start.next
        mid = mid.next

    return True


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(4)
    n6 = Node(3)
    n7 = Node(2)
    n8 = Node(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8

    mid = find_mid_point(n1)
    new_head = reverse(mid.next)
    mid.next = new_head
    print(is_palindromic(n1, new_head))
