from lists.node import Node


def print_list(head):
    while head:
        print(head.val)
        head = head.next


def delete(node):
    if node.next:
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    print_list(n1)
    delete(n4)
    print("--------------")
    print_list(n1)
