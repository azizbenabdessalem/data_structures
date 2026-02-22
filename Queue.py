from collections import deque

class Queue :
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.append(data)

    def dequeue(self):
        return self.buffer.popleft()

    def look_first(self):
        return self.buffer[0]

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
