class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        from collections import deque
        # time: O(K * V + E)
        # space: O(V + E)
        # method: Bellmon-Ford
        inf = float('inf')
        dist = [inf] * n
        dist[src] = 0
        queue = deque()
        queue.append((src, dist[src], 0))
        graph = {i: [] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))

        while queue:
            node, current_dist, stops = queue.popleft()
            if stops > k:
                continue
            for neighbor, weight in graph[node]:
                if current_dist + weight < dist[neighbor]:
                    dist[neighbor] = current_dist + weight
                    queue.append((neighbor, dist[neighbor], stops + 1))
        
        if dist[dst] == inf:
            return -1
        return dist[dst]