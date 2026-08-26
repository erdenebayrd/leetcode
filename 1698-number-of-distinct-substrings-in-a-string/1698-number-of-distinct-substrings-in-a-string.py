class Solution:
    def countDistinct(self, s: str) -> int:
        # time: O(N ^ 3)
        # space: O(N)
        # method: brute force

        n = len(s)
        seen = set()
        for left in range(n):
            for right in range(left, n):
                seen.add(s[left: right + 1])
        return len(seen)