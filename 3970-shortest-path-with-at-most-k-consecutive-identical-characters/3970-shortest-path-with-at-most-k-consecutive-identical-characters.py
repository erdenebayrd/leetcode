import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # time: O((V + E) * k * log ((V + E) * k) )
        # space: O((V + E) * k)
        # method: Dijkstra
        graph = {}
        for u, v, w in edges:
            if u not in graph:
                graph[u] = []
            
            graph[u].append((v, w))
        
        source = 0
        target = n - 1
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[source][1] = 0

        min_heap = [(dist[source][1], 1, source)]
        while min_heap:
            _, current_k, current_node = heapq.heappop(min_heap)
            if current_node not in graph:
                continue
                
            for next_node, weight in graph[current_node]:
                if labels[next_node] == labels[current_node]:
                    if current_k < k:
                        if dist[next_node][current_k + 1] > dist[current_node][current_k] + weight:
                            dist[next_node][current_k + 1] = dist[current_node][current_k] + weight
                            heapq.heappush(min_heap, (dist[next_node][current_k + 1], current_k + 1, next_node))
                else:
                    if dist[next_node][1] > dist[current_node][current_k] + weight:
                        dist[next_node][1] = dist[current_node][current_k] + weight
                        heapq.heappush(min_heap, (dist[next_node][1], 1, next_node))
        
        cost = min(dist[target])
        if cost == float('inf'):
            cost = -1
        return cost