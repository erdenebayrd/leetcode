from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # time: O(N)
        # space: O(N)
        # method: dfs + combinatoric

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        queue = deque()
        queue.append((1, 0))
        seen = set([1])
        slot = 0
        while queue:
            node, deep = queue.popleft()
            slot = max(slot, deep)
            for child in adj[node]:
                if child in seen:
                    continue
                seen.add(child)
                queue.append((child, deep + 1))
        
        return pow(2, slot - 1, 1_000_000_007)