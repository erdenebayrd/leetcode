class FenwickTree:
    def __init__(self, sz: int):
        self.ft = [0] * (sz + 1)
    
    def update(self, pos: int, delta: int) -> None:
        while pos < len(self.ft):
            self.ft[pos] += delta
            pos += -pos & pos
    
    def query(self, pos: int) -> int:
        res = 0
        while pos > 0:
            res += self.ft[pos]
            pos -= -pos & pos
        return res

class Solution:
    def goodTriplets(self, a: List[int], b: List[int]) -> int:
        # very similar to https://www.spoj.com/CSMS/problems/ERD0002/
        # time: O(N * Log N)
        # space: O(N)
        # method: Fenwick tree + something
        n = len(a)
        bPos = {}
        for i in range(n):
            bPos[b[i]] = i + 1
        prefixFt = FenwickTree(n)
        suffixFt = FenwickTree(n)
        for i in range(n):
            suffixFt.update(i + 1, 1)
        res = 0
        for i in range(n):
            idx = bPos[a[i]]
            suffixFt.update(idx, -1)
            # --------- calc ---------
            leftCount = prefixFt.query(idx - 1)
            rightCount = suffixFt.query(n) - suffixFt.query(idx)
            res += leftCount * rightCount
            # --------- calc ---------
            prefixFt.update(idx, 1)
        return res