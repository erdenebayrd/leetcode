class Solution:
    # def intTo32BitArray(self, x: int) -> List[int]:
    #     res = []
    #     for i in range(32):
    #         res.append((x >> i) & 1)
    #     return res

    # def init(self, arr):
    #     self.n = len(arr)
    #     self.arr = arr
    #     self.prefixBits = [self.intTo32BitArray(arr[0])]
    #     self.seen = {}
    #     for i in range(1, self.n):
    #         self.prefixBits.append(self.intTo32BitArray(arr[i]))
    #         for j in range(32):
    #             self.prefixBits[-1][j] += self.prefixBits[-2][j]

    # def rangeSumAt(self, idx: int, l: int, r: int) -> int:
    #     if l == 0:
    #         return self.prefixBits[r][idx]
    #     return self.prefixBits[r][idx] - self.prefixBits[l - 1][idx]

    # def getFirstIdxGapAt(self, bitIdx: int, l: int, r: int) -> int:
    #     lo, hi = l - 1, r + 1
    #     while lo + 1 < hi:
    #         md = (lo + hi) // 2
    #         if self.rangeSumAt(bitIdx, l, md) > 0:
    #             hi = md
    #         else:
    #             lo = md
    #     if hi == r + 1:
    #         hi = self.n
    #     return hi

    # def getFirstIdxGap(self, num: int, l: int, r: int) -> int:
    #     if l > r:
    #         return self.n
    #     idxs = []
    #     for i in range(32):
    #         if (num >> i) & 1:
    #             continue
    #         idxs.append(self.getFirstIdxGapAt(i, l, r))
    #     return min(idxs)

    # def solve(self, x: int, l: int, r: int) -> None:
    #     # if x in self.seen:
    #     #     return
    #     self.seen[x] = True
    #     idx = self.getFirstIdxGap(x, l, r)
    #     if idx >= self.n:
    #         return
    #     self.solve(self.arr[idx] | x, idx + 1, r)

    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # self.init(arr)
        # for i in range(self.n):
        #     self.solve(arr[i], i + 1, self.n - 1)
        # return len(self.seen)
        seen = set()
        suffix = set()
        for val in arr:
            cur = set()
            cur.add(val)
            for x in suffix: # at most 32
                cur.add(x | val)
            suffix = cur
            seen |= suffix
        return len(seen)