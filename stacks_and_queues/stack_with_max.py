class StackWithMax(object):
    def __init__(self):
        self.stack = []
        self.max_stack = []
        self.size = 0

    def push(self, elem):
        self.stack.append(elem)
        self.size += 1
        if (len(self.max_stack) > 0 and self.max_stack[-1] <= elem) or len(self.max_stack) == 0:
            self.max_stack.append(elem)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            elem = self.stack.pop()
            if elem == self.max_stack[-1]:
                self.max_stack.pop()
        return None

    def peek(self):
        if self.size > 0:
            return self.stack[-1]
        return None

    def get_max(self):
        if len(self.max_stack) > 0:
            return self.max_stack[-1]
        return None


if __name__ == "__main__":
    stack = StackWithMax()
    stack.push(1)
    print(stack.get_max())
    stack.push(2)
    print(stack.get_max())
    stack.push(3)
    print(stack.get_max())
    stack.push(5)
    print(stack.get_max())
    stack.push(4)
    print(stack.get_max())
    stack.push(7)
    print(stack.get_max())
    stack.pop()
    print(stack.get_max())
