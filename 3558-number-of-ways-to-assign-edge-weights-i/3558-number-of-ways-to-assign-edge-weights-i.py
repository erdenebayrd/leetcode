from collections import defaultdict

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # time: O(N)
        # space: O(h)
        # method: dfs + combinatoric

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node: int, parent: int) -> int:
            result = 0
            for child in adj[node]:
                if child == parent:
                    continue
                result = max(result, dfs(child, node))
            result += 1
            return result
        
        slot = dfs(1, 0) - 1
        return pow(2, slot - 1, 1_000_000_007)