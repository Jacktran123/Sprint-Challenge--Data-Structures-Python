class RingBuffer():
    def __init__(self, capacity):
        self.storage=[]
        self.capacity=capacity
        self.position=0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.position]=item
            self.position+=1
        if self.position == self.capacity:
            self.position=0

    def get(self):
        return self.storage
