class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        vis = [False] * n
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # print(graph)
        def dfs(x: int) -> tuple:
            node = 1
            edge = len(graph[x])
            vis[x] = True
            for ch in graph[x]:
                if vis[ch] is True:
                    continue
                chNode, chEdge = dfs(ch)
                node += chNode
                edge += chEdge
            return (node, edge)
        
        res = 0
        for i in range(n):
            if vis[i] is True:
                continue
            node, edge = dfs(i)
            if node * (node - 1) == edge:
                res += 1
        return res