class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        arr = []
        for i in range(32):
            arr.append(str(1 << i))
        n = str(n)
        for x in arr:
            if Counter(x) == Counter(n):
                return True
        return False