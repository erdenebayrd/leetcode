class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # time: O(len(roads) + n ^ 2)
        # space: O(n + len(roads))
        # method: brute force
        degree = [0] * n
        connected = [set() for _ in range(n)]
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
            connected[u].add(v)
            connected[v].add(u)
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                current = degree[i] + degree[j]
                if j in connected[i]:
                    current -= 1
                result = max(result, current)
        return result