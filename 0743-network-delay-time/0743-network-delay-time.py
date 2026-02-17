import heapq
from typing import List
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        dijkstra 
        time: O((V + E) * LogV) use heap
        space: O(V + E) we use distance for each node + adjacent list for graph representation (edges)
        starting from k
        distances would become min distance from k -> all other nodes
        max(distances) would be the answer
        if we can't reach the all nodes from k, return -1
        Example 1:
            
            Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
            Output: 2
            
            n = 4
            k = 2
               
                1
           "2" ---> 1
            |
          1 |
            |
            V 
            3 ---> 4
               1

        """


        # Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        # Output: 2
        def dijkstra(graph, k: int, n: int): # max(distances) from node k, n is the total nodes of the graph
            distances = [float('inf')] * (n + 1)
            # index              0,   1,   2,   3,   4
            distances[k] = 0 # [inf, inf,  0, inf, inf]
            minHeap = []
            heapq.heappush(minHeap, [distances[k], k]) # [[0, 2]]

            while minHeap: # O(N * Log N) -> O((V + E) * Log V)
                _, node = heapq.heappop(minHeap) # [ ] node = 2
                for neighbor, weight in graph[node]: # 2 -> 1, 2 -> 3, weight = 1
                    if distances[neighbor] > distances[node] + weight:
                        distances[neighbor] = distances[node] + weight
                        heapq.heappush(minHeap, [distances[neighbor], neighbor])
            result = 0
            for node in range(1, n + 1):
                result = max(result, distances[node])

            return result

        
        graph = defaultdict(list)
        for nodeU, nodeV, weight in times:
            graph[nodeU].append([nodeV, weight])
        
        result = dijkstra(graph, k, n)
        if result == float('inf'):
            result = -1
        return result