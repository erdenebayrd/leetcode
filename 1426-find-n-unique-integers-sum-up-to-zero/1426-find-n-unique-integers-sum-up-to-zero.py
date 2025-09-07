class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        m = n // 2
        for i in range(m):
            arr.append(i + 1)
            arr.append(-i - 1)
        if n & 1:
            arr.append(0)
        return arr