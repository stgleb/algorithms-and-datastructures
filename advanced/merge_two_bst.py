class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val)
    inorder_traversal(root.right)


def merge(root1, root2):
    if root1 is None and root2 is None:
        return

    if root1 is None:
        inorder_traversal(root2)
        return

    if root2 is None:
        inorder_traversal(root1)
        return root1

    tmp1 = root1
    prev1 = None

    while tmp1.left:
        prev1 = tmp1
        tmp1 = tmp1.left

    tmp2 = root2
    prev2 = None
    while tmp2.left:
        prev2 = tmp2
        tmp2 = tmp2.left

    if tmp1.val <= tmp2.val:
        print(tmp1.val)
        if prev1 is None:
            merge(root1.right, root2)
        else:
            prev1.left = tmp1.right
            merge(root1, root2)
    else:
        print(tmp2.val)
        if prev2 is None:
            merge(root1, root2.right)
        else:
            prev2.left = tmp2.right
            merge(root1, root2)


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n4.left = n2
    n4.right = n6
    n3.left = n1
    n3.right = n5
    n5.right = n7
    new_root = merge(n4, n3)
    inorder_traversal(new_root)

