class QueueWithMax(object):
    def __init__(self):
        self.queue = []
        self.max_queue = []

    def push(self, elem):
        self.queue.append(elem)
        if len(self.max_queue) == 0:
            self.max_queue.append(elem)
        else:
            while len(self.max_queue) > 0 and self.max_queue[-1] < elem:
                self.max_queue.pop()
            self.max_queue.append(elem)

    def pop(self):
        if len(self.queue) == 0:
            return None
        elem = self.queue[0]
        self.queue = self.queue[1:]
        if elem == self.max_queue[0]:
            self.max_queue = self.max_queue[1:]
        return elem

    def max(self):
        if len(self.max_queue) == 0:
            return None
        return self.max_queue[0]


if __name__ == "__main__":
    q = QueueWithMax()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.max())
    q.push(2)
    q.pop()
    q.pop()
    print(q.max())
    q.pop()
    print(q.max())
    q.push(4)
    print(q.max())
