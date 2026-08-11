class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # time: O(N + len(dislikes))
        # space: O(N + len(dislikes))
        # method: coloring (dfs) black & white
        adj = defaultdict(list)
        colors = [-1] * (n + 1)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
        
        def paint(node: int, color: int) -> bool:
            if colors[node] != -1:
                return colors[node] == color

            colors[node] = color
            for neighbor in adj[node]:
                if not paint(neighbor, color ^ 1):
                    return False
            return True

        
        for i in range(1, n + 1):
            if colors[i] == -1:
                if not paint(i, 0):
                    return False
        return True