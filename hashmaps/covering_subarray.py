class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class List(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = None
        self.size = 0

    def append(self, node):
        self.size += 1
        if self.tail is None:
            self.head.next, self.tail = node, node
            self.tail.prev = self.head
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = self.tail.next

    def push_to_front(self, node):
        if node is self.tail:
            return

        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = self.tail.next


def min_covering_subarray(text, words):
    text_words = list(text.split(" "))
    d = {}
    l = List()
    min_val = len(text_words)

    for i in range(len(text_words)):
        if text_words[i] in words:
            if text_words[i] not in d:
                node = Node(i)
                d[text_words[i]] = node
                l.append(node)
            else:
                node = d[text_words[i]]
                node.val = i
                l.push_to_front(node)
        if l.size == len(words) and l.tail.val - l.head.next.val < min_val:
            min_val = l.tail.val - l.head.next.val
    return min_val


if __name__ == "__main__":
    print(min_covering_subarray("paramount object in the struggle is to save the union and "
                                "is not either union destroy or save slavery",
                                {"save", "union", "slavery"}))
