class Solution:
    def init(self, k: int) -> None: # top k
        self.top = SortedList([])
        self.rest = SortedList([])
        self.fq = defaultdict(int)
        self.cur = 0
        self.k = k
    
    def update(self, val: int, delta: int) -> None:
        cur = (self.fq[val], val)
        if cur in self.top:
            self.top.remove(cur)
            self.cur -= cur[0] * cur[1]
        if cur in self.rest:
            self.rest.remove(cur)
        self.fq[val] += delta
        cur = (self.fq[val], val)
        self.rest.add(cur)
        if len(self.top) < self.k:
            self.top.add(self.rest[-1])
            self.cur += self.rest[-1][0] * self.rest[-1][1]
            self.rest.pop(-1)
        elif self.top[0][0] < self.rest[-1][0] or (self.top[0][0] == self.rest[-1][0] and self.top[0][1] < self.rest[-1][1]):
            self.rest.add(self.top[0])
            self.cur -= self.top[0][0] * self.top[0][1]
            self.top.pop(0)
            self.cur += self.rest[-1][0] * self.rest[-1][1]
            self.top.add(self.rest[-1])
            self.rest.pop(-1)

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        self.init(x)
        res = []
        for i in range(k):
            self.update(nums[i], 1)
        for i in range(k, len(nums)):
            res.append(self.cur)
            self.update(nums[i], 1)
            self.update(nums[i - k], -1)
        res.append(self.cur)
        return res