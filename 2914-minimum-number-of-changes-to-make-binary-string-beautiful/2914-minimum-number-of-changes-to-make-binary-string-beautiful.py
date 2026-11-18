class Solution:
    def minChanges(self, s: str) -> int:
        # time: O(N)
        # space: O(1)
        # method: iteration
        n = len(s)
        result = 0
        for i in range(1, n, 2):
            result += int(s[i] != s[i - 1])
        return result