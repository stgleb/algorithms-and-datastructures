class Node(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right


def generate_binary_tree(num_nodes):
    if num_nodes == 0:
        return [None]
    result = []
    for i in range(num_nodes):
        left_trees = generate_binary_tree(i)
        right_trees = generate_binary_tree(num_nodes - i - 1)
        for l in left_trees:
            for r in right_trees:
                result.append(Node(l, r))
    return result


if __name__ == "__main__":
    print(len(generate_binary_tree(3)))
