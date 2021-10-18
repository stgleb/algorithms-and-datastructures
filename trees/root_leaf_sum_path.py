from trees.node import Node


def sum_path_util(root, target_sum, path=[], path_sum=0):
    if path_sum == target_sum:
        path.pop()
        return path
    if root is None:
        return None

    path.append(root.left)
    result_path = sum_path_util(root.left, target_sum, path, path_sum + root.val)
    if result_path is not None:
        return result_path
    path.pop()

    path.append(root.right)
    result_path = sum_path_util(root.right, target_sum, path, path_sum + root.val)
    path.pop()
    if result_path is not None:
        return result_path


def sum_path(root, target_sum):
    return sum_path_util(root, target_sum, path=[root], path_sum=0)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(3)
    node6 = Node(2)
    node7 = Node(1)

    node4.left = node2
    node2.left = node1
    node2.right = node3
    node4.right = node6
    node6.left = node5
    node6.right = node7
    print([x.val for x in sum_path(node4, 7)])
