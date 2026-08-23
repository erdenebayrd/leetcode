class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # time: O(m * log (n * m))
        # space: O(1)
        # method: binary search
        low, high = 0, n * m + 1
        while low + 1 < high:
            mid = (low + high) // 2
            count = 0
            for i in range(1, m + 1):
                count += min(mid // i, n)
            if count < k:
                low = mid
            else:
                high = mid
        return high
