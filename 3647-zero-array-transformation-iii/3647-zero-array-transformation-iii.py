class FenwickTree:
    def __init__(self, n: int) -> None:
        self.ft = [0] * (n + 2)
    
    def update(self, pos: int, val: int) -> None:
        while pos < len(self.ft):
            self.ft[pos] += val
            pos += -pos & pos

    def get(self, pos: int) -> int:
        res = 0
        while pos > 0:
            res += self.ft[pos]
            pos -= -pos & pos
        return res

    def query(self, l: int, r: int) -> int:
        return self.get(r) - self.get(l - 1)

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        appliedQueriesFt = FenwickTree(len(nums))
        currentQueries = []
        queries.sort()
        st = {}
        for l, r in queries:
            if l not in st:
                st[l] = []
            st[l].append(r + 1)
        for i in range(len(nums)):
            # print(appliedQueriesFt.query(i + 1, len(nums)))
            if i in st:
                for r in st[i]:
                    heapq.heappush(currentQueries, -r)
            x = appliedQueriesFt.query(i + 1, len(nums))
            x = nums[i] - x
            if x <= 0:
                continue

            while x > 0 and len(currentQueries) > 0:
                r = -heapq.heappop(currentQueries)
                if r >= i + 1:
                    x -= 1
                    appliedQueriesFt.update(r, 1)
                    continue
                return -1
            # print(x)
            if x > 0:
                return -1
        return len(queries) - appliedQueriesFt.query(1, len(nums))