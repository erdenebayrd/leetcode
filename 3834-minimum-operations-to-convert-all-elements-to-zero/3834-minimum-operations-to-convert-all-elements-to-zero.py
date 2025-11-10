class Solution:
    def init(self, nums):
        self.pos = {}
        self.nums = nums
        self.n = len(nums)
        self.st = [0] * self.n * 4
        for i, x in enumerate(nums):
            if x not in self.pos:
                self.pos[x] = []
            self.pos[x].append(i)
        self.build(1, 0, self.n - 1)
    
    def build(self, p, l, r):
        if l == r:
            self.st[p] = self.nums[r]
            return
        self.build(2 * p, l, (l + r) // 2)
        self.build(2 * p + 1, (l + r) // 2 + 1, r)
        self.st[p] = min(self.st[2 * p], self.st[2 * p + 1])
    
    def get(self, p, l, r, L, R):
        if l > r or l > R or r < L:
            return int(1e18)
        if l >= L and r <= R:
            return self.st[p]
        return min(self.get(2 * p, l, (l + r) // 2, L, R), self.get(2 * p + 1, (l + r) // 2 + 1, r, L, R))

    def solve(self, l, r) -> int:
        if l > r:
            return 0
        if l == r:
            return 1 if self.nums[r] > 0 else 0
        mn = self.get(1, 0, self.n - 1, l, r)
        le = bisect.bisect_left(self.pos[mn], l)
        ri = bisect.bisect_right(self.pos[mn], r) - 1
        # self.pos[mn][le] -> self.pos[mn][ri]
        res = 1 if mn > 0 else 0
        res += self.solve(l, self.pos[mn][le] - 1)
        for i in range(le, ri):
            res += self.solve(self.pos[mn][i] + 1, self.pos[mn][i + 1] - 1)
        res += self.solve(self.pos[mn][ri] + 1, r)
        return res
        

    def minOperations(self, nums: List[int]) -> int:
        self.init(nums)
        return self.solve(0, self.n - 1)