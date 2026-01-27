import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # V -> number of vertices
        # E -> number of edges
        # time complexity O((V + E) * log V)
        # space complexity O(V + E)
        def dijkstra(start_node: int, destination_node: int, adjacent_list: List[List[int, int]]) -> int:
            inf = float('inf')
            distances = [inf] * n
            distances[start_node] = 0
            min_heap = [(distances[start_node], start_node)]
            heapq.heapify(min_heap)
            while min_heap:
                _, current_node = heapq.heappop(min_heap)
                for next_node, cost in adjacent_list[current_node]:
                    if distances[next_node] > distances[current_node] + cost:
                        distances[next_node] = distances[current_node] + cost
                        heapq.heappush(min_heap, (distances[next_node], next_node))
            if distances[destination_node] == inf:
                return -1
            return distances[destination_node]
        
        adjacent_list = [[] for _ in range(n)]
        for u, v, w in edges:
            # u -> v with w cost
            adjacent_list[u].append([v, w])
            # u <- v with 2 * w cost
            adjacent_list[v].append([u, 2 * w])
        
        return dijkstra(0, n - 1, adjacent_list)