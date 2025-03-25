class MovingAverage:

    def __init__(self, size: int):
        self.sz = size
        self.queue = deque()
        self.curSum = 0

    def next(self, val: int) -> float:
        if len(self.queue) < self.sz:
            self.curSum += val
            self.queue.append(val)
        else:
            self.curSum -= self.queue.popleft()
            self.curSum += val
            self.queue.append(val)
        return self.curSum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)