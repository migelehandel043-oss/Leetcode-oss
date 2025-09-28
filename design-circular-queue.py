class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [0] * k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            # Queue will be empty after this operation
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front
# Initialize circular queue with size 3
myCircularQueue = MyCircularQueue(3)

print(myCircularQueue.enQueue(1))  # True
print(myCircularQueue.enQueue(2))  # True
print(myCircularQueue.enQueue(3))  # True
print(myCircularQueue.enQueue(4))  # False (queue full)
print(myCircularQueue.Rear())      # 3
print(myCircularQueue.isFull())    # True
print(myCircularQueue.deQueue())   # True
print(myCircularQueue.enQueue(4))  # True
print(myCircularQueue.Rear())      # 4
