class CustomStack:

    def __init__(self, maxSize: int):
        # initialize with max size and empty stack
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        # push only if size not exceeded
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        # pop top element or return -1 if empty
        if not self.stack:
            return -1
        return self.stack.pop()

    def inc(self, k: int, val: int) -> None:
        # increment bottom k elements by val
        limit = min(k, len(self.stack))
        for i in range(limit):
            self.stack[i] += val

stack = CustomStack(5)
stack.push(1)
stack.push(2)
print(stack.pop())      # 2
stack.push(2)
stack.push(3)
stack.push(4)
stack.inc(5, 100)       # increment all elements
stack.inc(2, 100)       # increment bottom 2 elements
print(stack.pop())      # 103
print(stack.pop())      # 102
print(stack.pop())      # 201
print(stack.pop())      # -1 (empty)
