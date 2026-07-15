
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = ((n - 1) * n // 2) * 2 + n
        even = (n * (n + 1) // 2) * 2
        return gcd(odd, even)