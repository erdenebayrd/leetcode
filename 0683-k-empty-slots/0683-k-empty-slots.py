class FenwickTree:
    def __init__(self, defaultValue: int, sz: int) -> None:
        self.tree = [defaultValue] * (sz + 1)
    
    def update(self, pos: int, val: int) -> None:
        while pos < len(self.tree):
            self.tree[pos] += val
            pos += pos & -pos
    
    def prefixSum(self, pos: int) -> int:
        res = 0
        while pos > 0:
            res += self.tree[pos]
            pos -= pos & -pos
        return res
    
    def rangeSum(self, l: int, r: int) -> int:
        assert l - 1 >= 0
        return self.prefixSum(r) - self.prefixSum(l - 1)
    
    def get(self, pos: int) -> int:
        return self.rangeSum(pos, pos)

class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        n = len(bulbs)
        ft = FenwickTree(defaultValue = 0, sz = n)
        for day, pos in enumerate(bulbs):
            ft.update(pos, 1)
            if pos - k - 1 > 0 and ft.get(pos - k - 1) == 1 and ft.rangeSum(pos - k, pos - 1) == 0:
                return day + 1
            if pos + k + 1 <= n and ft.get(pos + k + 1) == 1 and ft.rangeSum(pos + 1, pos + k) == 0:
                return day + 1
        return -1