class PriorityQueue:
    def __init__(self, l=[], key=None):
        self.queue = sorted(l, key=key)

    def enqueue(self, e):
        if len(self.queue) == 0:
            self.queue = [e]
            return self.queue

        start = 0
        end = len(self.queue)
        m = (start+end/2)

        while start+1 != end:
            if e > self.queue[m]:
                start = m  
            else:
                end = m
            m = (start+end)/2

        if e > self.queue[m]:
            m += 1
        self.queue = self.queue[:m] + [e] + self.queue[m:]
        return self.queue

    def dequeue(self):
        e, self.queue = self.queue[0], self.queue[1:]
        return e

    def __repr__(self):
        return self.queue.__repr__()

    def __len__(self):
        return len(self.queue)
