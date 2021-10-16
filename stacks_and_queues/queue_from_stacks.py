class StackedQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, elem):
        self.stack1.append(elem)

    def pop(self):
        if len(self.stack2) > 0:
            return self.stack2.pop()
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        if len(self.stack2) > 0:
            return self.stack2.pop()
        return None


if __name__ == "__main__":
    q = StackedQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
