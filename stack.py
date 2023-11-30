class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)


# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)
print("Pop:", stack.pop())
print("Peek:", stack.peek())
print("Size:", stack.size())

queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

print("\nQueue:", queue.items)
print("Dequeue:", queue.dequeue())
print("Peek:", queue.peek())
print("Size:", queue.size())
