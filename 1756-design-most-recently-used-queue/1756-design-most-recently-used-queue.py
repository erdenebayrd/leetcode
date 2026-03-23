class FenwickTree:
    def __init__(self, size: int) -> int:
        self.ft = [0] * size # O(N)
    
    def update(self, pos: int, val: int) -> None: # O(log n)
        while pos < len(self.ft):
            self.ft[pos] += val
            pos += -pos & pos
    
    def query(self, right: int) -> int: # O(log n)
        result = 0
        while right > 0:
            result += self.ft[right]
            right -= -right & right
        return result

from sortedcontainers import SortedList

class MRUQueue:

    def __init__(self, n: int): # O(n log n)
        # self.ones = FenwickTree(n + 2001)
        # self.nums = FenwickTree(n + 2001)
        # self.nextPosition = n + 1
        # for i in range(1, n + 1):
        #     self.ones.update(i, 1)
        #     self.nums.update(i, i)
        self.queue = SortedList((i, i) for i in range(1, n + 1))
        self.next = n + 1

    def fetch(self, k: int) -> int: # O(log n * log n)
        # low, high = 0, self.nextPosition
        # while low + 1 < high:
        #     mid = (low + high) // 2
        #     if self.ones.query(mid) >= k:
        #         high = mid
        #     else:
        #         low = mid
        # position = high
        # number = self.nums.query(position) - self.nums.query(position - 1)
        # # remove from ft
        # self.ones.update(position, -1)
        # self.nums.update(position, -number)

        # # adding to ft
        # self.ones.update(self.nextPosition, 1)
        # self.nums.update(self.nextPosition, number)
        # self.nextPosition += 1
        # return number

        _, value = self.queue.pop(k - 1)
        self.queue.add((self.next, value))
        self.next += 1

        return value

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)