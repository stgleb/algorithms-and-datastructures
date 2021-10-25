class Node(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class List(object):
    def __init__(self):
        self.head = Node(None, None)
        self.tail = None

    def append(self, node):
        if self.tail is None:
            self.head.next = node
            node.prev = self.head
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def push_to_front(self, node):
        if node is None:
            return

        if self.tail is node:
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = self.tail.next

    def evict(self):
        node = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return node


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.list = List()

    def get(self, key):
        if key not in self.map:
            return None

        node = self.map[key]
        self.list.push_to_front(node)
        if node:
            return node.val
        return None

    def set(self, key, value):
        if key in self.map:
            node = self.map[key]
            self.list.push_to_front(node)
            return

        if self.size == self.capacity:
            node = self.list.evict()
            del self.map[node.key]
        else:
            self.size += 1
        node = Node(key, value)
        self.list.append(node)
        self.map[key] = node


if __name__ == "__main__":
    cache = LRUCache(3)
    cache.set(1, "hello")
    cache.set(2, "world")
    cache.set(3, "!!!")
    cache.set(4, "!!!")

    print(cache.get(1))
    print(cache.get(2))
    print(cache.get(3))
    print(cache.get(4))
    print(cache.get(2))
    cache.set(5, "match")
    cache.set(6, "all")
    print(cache.get(5))
    print(cache.get(6))
    print(cache.get(2))
    print(cache.get(4))
    print(cache.get(3))
