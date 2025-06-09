class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def calc(n, curr, next):
            total = 0
            while curr <= n:
                total += min(n + 1, next) - curr
                curr *= 10
                next *= 10
            return total

        curr = 1
        k -= 1 
        while k > 0:
            count = calc(n, curr, curr + 1)
            if count <= k:
                k -= count
                curr += 1
            else:
                k -= 1
                curr *= 10
        return curr