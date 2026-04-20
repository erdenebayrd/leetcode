class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # time: O(N ^ 3)
        # space: O(N ^ 2)
        # method: graph dfs
        # build directed graph first
        adj = defaultdict(list)
        n = len(bombs)

        def distance(i: int, j: int) -> int:
            xi, yi, _ = bombs[i]
            xj, yj, _ = bombs[j]
            return (xi - xj) ** 2 + (yi - yj) ** 2

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                _, _, radius = bombs[i]
                if distance(i, j) <= radius * radius:
                    adj[i].append(j)

        # @cache
        def dfs(node: int) -> int:
            visited[node] = True
            result = 1
            for neighbor in adj[node]:
                if visited[neighbor]:
                    continue
                result += dfs(neighbor)
            return result
        
        result = 0
        for i in range(n):
            visited = defaultdict(bool)
            result = max(result, dfs(i))
        return result