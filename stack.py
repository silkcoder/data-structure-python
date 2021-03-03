class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
