class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bst_to_list(root):
    if root is None:
        return None, None

    l_start, l_end = bst_to_list(root.left)
    r_start, r_end = bst_to_list(root.right)

    if l_start is None:
        l_start = root

    if l_end is None:
        l_end = root

    if r_start is None:
        r_start = root

    if r_end is None:
        r_end = root

    root.left = l_end
    l_end.right = root
    root.right = r_start
    r_start.left = root

    return l_start, r_end


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n4.left = n2
    n2.left = n1
    n2.right = n3
    n4.right = n6
    n6.left = n5
    n6.right = n7
    start, end = bst_to_list(n4)
    end.right = None
    
    while start:
        print(start.val)
        start = start.right
