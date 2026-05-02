class Solution:
    def maxDistance(self, words: List[str]) -> int:
        # time: O(N)
        # space: O(1)
        # method: greedy

        n = len(words)
        result = 0
        for i in range(n - 1, -1, -1):
            if words[0] != words[i]:
                result = max(result, i + 1)
                break

        for i in range(n):
            if words[n - 1] != words[i]:
                result = max(result, n - i)
                break

        return result