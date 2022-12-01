class Queue:
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def peek(self):
        return self.queue[0]

    def enqueue(self, value):
        return self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def search(self, index):
        if index < 0 or index > len(self.queue):
            raise IndexError
        return self.queue[index]
