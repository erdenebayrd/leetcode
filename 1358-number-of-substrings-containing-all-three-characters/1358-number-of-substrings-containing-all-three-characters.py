class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # time: O(N)
        # space: O(1)
        # method: sliding window
        count = {"a": 0, "b": 0, "c": 0}
        left = 0
        result = 0
        n = len(s)
        for right in range(n):
            count[s[right]] += 1
            while min(count.values()) > 0:
                result += n - right
                count[s[left]] -= 1
                left += 1
        return result