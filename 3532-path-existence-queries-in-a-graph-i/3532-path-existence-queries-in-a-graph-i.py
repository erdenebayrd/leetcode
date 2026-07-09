class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # time: O(N + Q)
        # space: O(N)
        # method: sliding window + graph comp
        comps = [0] * n
        current = 0
        right = 0
        for left in range(n):
            if left == right:
                current += 1
            while right < n and nums[right] - nums[left] <= maxDiff:
                comps[right] = current
                right += 1
        result = []
        for u, v in queries:
            result.append(comps[u] == comps[v])
        return result