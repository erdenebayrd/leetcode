from collections import deque

class HitCounter:
    # time: O(N + M) N is the number of calls made to hit, M is number of calls of getHits
    # space: O(N + M)
    def __init__(self):
        self.logs = deque()

    def expire(self, timestamp: int) -> None:
        while self.logs and self.logs[0] + 300 <= timestamp:
            self.logs.popleft()

    def hit(self, timestamp: int) -> None:
        self.logs.append(timestamp)
        self.expire(timestamp)

    def getHits(self, timestamp: int) -> int:
        self.expire(timestamp)
        return len(self.logs)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)