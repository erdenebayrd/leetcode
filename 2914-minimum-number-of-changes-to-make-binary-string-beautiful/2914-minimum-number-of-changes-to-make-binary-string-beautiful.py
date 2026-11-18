class Solution:
    def minChanges(self, s: str) -> int:
        # time: O(N)
        # space: O(1)
        # method: iteration
        prev = 0
        curr = 1
        n = len(s)
        result = 0
        for i in range(1, n):
            if s[i - 1] != s[i]:
                prev = curr & 1
                result += prev
                curr = prev
            curr += 1
        result += (curr & 1)
        return result