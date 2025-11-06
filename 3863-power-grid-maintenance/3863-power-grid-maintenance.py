class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        comps = [SortedList([]) for _ in range(c)]
        comp = [-1] * c
        graph = [[] for _ in range(c)]
        for u, v in connections:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        vis = [False] * c
        
        def dfs(u: int, compId: int) -> None:
            comp[u] = compId
            comps[compId].add(u)
            vis[u] = True
            for v in graph[u]:
                if vis[v] is True:
                    continue
                dfs(v, compId)
        
        curCompId = 0
        for i in range(c):
            if vis[i] is True:
                continue
            dfs(i, curCompId)
            curCompId += 1
        
        # print(comps)
        # print(comp)

        res = []
        for t, v in queries:
            v -= 1
            if t == 1: # maintenance check
                if v in comps[comp[v]]:
                    res.append(v + 1)
                elif len(comps[comp[v]]) > 0:
                    res.append(comps[comp[v]][0] + 1)
                else:
                    res.append(-1)
            else: # goes offline
                comps[comp[v]].discard(v)

        return res
        