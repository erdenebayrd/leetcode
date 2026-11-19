class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # time: O(K * V + E)
        # space: O(V + E)
        # method: Bellmon-Ford
        inf = float('inf')
        dist = [inf] * n
        dist[src] = 0
        for _ in range(k + 1):
            tmp = dist[:]
            for u, v, w in flights:
                if dist[u] + w < tmp[v]:
                    tmp[v] = dist[u] + w
            dist = tmp
        
        if dist[dst] == inf:
            return -1
        return dist[dst]