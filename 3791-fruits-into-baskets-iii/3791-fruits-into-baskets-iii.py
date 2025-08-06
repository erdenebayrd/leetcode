class SegmentTree:
    def build(self, p: int, l: int, r: int) -> None:
        if l == r:
            self.st[p] = self.arr[r]
            return
        self.build(2 * p, l, (l + r) // 2)
        self.build(2 * p + 1, (l + r) // 2 + 1, r)
        self.st[p] = min(self.st[2 * p], self.st[2 * p + 1])

    def __init__(self, n: int, arr: List[int]) -> None:
        self.n = n
        self.st = [max(arr) + 1] * n * 4
        self.arr = arr
        self.build(1, 0, n - 1)
    
    def update(self, p: int, l: int, r: int, idx: int, val: int) -> None:
        if l > r or l > idx or r < idx:
            return
        if l == r and r == idx:
            self.st[p] = val
            return
        self.update(2 * p, l, (l + r) // 2, idx, val)
        self.update(2 * p + 1, (l + r) // 2 + 1, r, idx, val)
        self.st[p] = min(self.st[2 * p], self.st[2 * p + 1])

    def rmq(self, p: int, l: int, r: int, L: int, R: int) -> int:
        if l > r or l > R or r < L or L > R:
            return self.n
        if l >= L and r <= R:
            return self.st[p]
        res = self.rmq(2 * p, l, (l + r) // 2, L, R)
        res = min(res, self.rmq(2 * p + 1, (l + r) // 2 + 1, r, L, R))
        return res

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # time: O(N * Log N)
        # space: O(N)
        # method: rmq
        n = len(fruits)
        arr = []
        for i in range(n):
            arr.append([baskets[i], i])
        arr.sort()
        pos = {}
        for i in range(len(arr)):
            pos[arr[i][1]] = i
        objSt = SegmentTree(n, [x for _, x in arr])
        res = n
        for x in fruits:
            le = bisect_left(arr, x, key=lambda x: x[0])
            idx = objSt.rmq(1, 0, n - 1, le, n - 1)
            # print(idx)
            if idx == n:
                continue
            res -= 1
            objSt.update(1, 0, n - 1, pos[idx], n)
        return res