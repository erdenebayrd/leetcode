class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for u, v in invocations:
            adj[u].append(v)
            indegree[v] += 1
        
        visited = set()

        def dfs(node: int) -> None:
            visited.add(node)
            for ch in adj[node]:
                indegree[ch] -= 1
                if ch in visited:
                    continue
                dfs(ch)
        
        dfs(k)

        for node in visited:
            if indegree[node] > 0:
                return [x for x in range(n)]
        
        result = []
        for i in range(n):
            if i in visited:
                continue
            result.append(i)
        return result