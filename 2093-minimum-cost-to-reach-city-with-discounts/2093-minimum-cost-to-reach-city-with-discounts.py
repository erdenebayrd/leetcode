import heapq

class Solution:
    def minimumCost(self, n: int, highways: list[list[int]], discounts: int) -> int:
        # time: O((E + V log V) * discounts)
        # space: O(V + E)
        # method: Dijkstra

        graph = [[] for _ in range(n)]
        for u, v, w in highways:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        inf = float('inf')

        dist = [[inf] * (discounts + 1) for _ in range(n)]
        dist[0][discounts] = 0
        min_heap = [(dist[0][discounts], 0, discounts)]

        while min_heap:
            _, node, current_discounts = heapq.heappop(min_heap)
            for neighbor, toll in graph[node]:
                # no discount usage
                if dist[neighbor][current_discounts] > dist[node][current_discounts] + toll:
                    dist[neighbor][current_discounts] = dist[node][current_discounts] + toll
                    heapq.heappush(min_heap, (dist[neighbor][current_discounts], neighbor, current_discounts))

                # using discount
                if current_discounts > 0 and dist[neighbor][current_discounts - 1] > dist[node][current_discounts] + toll // 2:
                    dist[neighbor][current_discounts - 1] = dist[node][current_discounts] + toll // 2
                    heapq.heappush(min_heap, (dist[neighbor][current_discounts - 1], neighbor, current_discounts - 1))
        
        cost = min(dist[n - 1])
        if cost == inf:
            cost = -1
        return cost