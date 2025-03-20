class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # time: O(N)
        # space: O(N)
        graph = defaultdict(list[int])
        for u, v, _ in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        vis = [False] * n
        comp = defaultdict(int)
        def dfs(x: int, curComp: int):
            comp[x] = curComp
            vis[x] = True
            for ch in graph[x]:
                if vis[ch] is True:
                    continue
                dfs(ch, curComp)
        curComp = 0
        for vertex in range(n):
            if vis[vertex] is True:
                continue
            curComp += 1
            dfs(vertex, curComp)
        # print(comp)

        compEdges = defaultdict(lambda: (1 << 20) - 1)
        for u, v, w in edges:
            assert comp[u] == comp[v]
            compEdges[comp[v]] &= w
        
        res = []
        for s, t in query:
            if comp[s] != comp[t]:
                res.append(-1)
                continue
            res.append(compEdges[comp[s]])
        return res