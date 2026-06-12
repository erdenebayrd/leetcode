from collections import defaultdict

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # time: O(N log N)
        # space: O(N log N)
        # method: LCA

        n = len(edges) + 1
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        m = int(log2(n)) + 1
        parents = [[0] * m for _ in range(n + 1)]
        level = [0] * (n + 1)
        def dfs(node: int, parent: int, deep: int) -> None:
            level[node] = deep
            parents[node][0] = parent
            for child in adj[node]:
                if child == parent:
                    continue
                dfs(child, node, deep + 1)
        
        dfs(1, 0, 0)
        for i in range(1, m):
            for node in range(1, n + 1):
                parents[node][i] = parents[parents[node][i - 1]][i - 1]
        
        mod = 1_000_000_007
        result = []
        for u, v in queries:
            if u == v:
                result.append(0)
                continue
            count_edges = abs(level[u] - level[v])
            while level[u] != level[v]:
                diff = abs(level[u] - level[v])
                par = int(log2(diff))
                if level[u] > level[v]:
                    u, v = v, u
                v = parents[v][par]
            if u == v:
                result.append(pow(2, count_edges - 1, mod))
                continue
            for i in range(m - 1, -1, -1):
                if parents[u][i] != parents[v][i]:
                    u, v = parents[u][i], parents[v][i]
                    count_edges += (1 << (i + 1))
            count_edges += 2
            result.append(pow(2, count_edges - 1, mod))

        return result