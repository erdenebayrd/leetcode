class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        # time: O(N * Log N)
        # space: O(N ^ 2)
        # dijkstra
        inf = int(1e9)
        graph = defaultdict(list)
        distArr = [[inf] * n for _ in range(n)]
        for u, v, w in edges:
            distArr[u][v] = min(distArr[u][v], w)
        for u, v, w in edges:
            graph[u].append((v, distArr[u][v]))
        
        def dijkstra():
            dist = [inf] * n
            dist[s] = 0
            arr = [(dist[s], s)]
            heapq.heapify(arr)
            while len(arr) > 0:
                _, u = heapq.heappop(arr)
                for v, w in graph[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heapq.heappush(arr, (dist[v], v))
            return dist
        
        dist = dijkstra()
        res = inf
        for v in marked:
            res = min(res, dist[v])
        if res == inf:
            res = -1
        
        return res