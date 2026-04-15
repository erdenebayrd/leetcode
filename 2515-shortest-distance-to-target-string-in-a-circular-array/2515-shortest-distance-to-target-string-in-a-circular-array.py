class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # time: O(N + M)
        # space: O(1)
        # method: search
        n = len(words)
        result = float('inf')
        for i in range(n):
            word = words[i]
            if word == target:
                distance = min(abs(startIndex - i), min(startIndex, i) + n - max(startIndex, i))
                result = min(result, distance)
        if result == float('inf'):
            result = -1
        return result