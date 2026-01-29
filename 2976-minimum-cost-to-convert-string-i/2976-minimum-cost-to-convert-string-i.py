import heapq
from typing import List, Tuple

class Solution:
    def dijkstra(self, sourceNodeNumber: int) -> List[int]: # time: O((V + E) * Log(V)), V number of vertices which is 26, E is number of edges, which could reach 2000, space complexity: O(V+E)
        # self.adjacentList: List[Tuple[int, int]]
        distances = [float('inf')] * 26
        # priorityQueue
        minHeap = []
        distances[sourceNodeNumber] = 0
        heapq.heappush(minHeap, (distances[sourceNodeNumber], sourceNodeNumber))
        while minHeap:
            _, currentNode = heapq.heappop(minHeap)
            for neighborNode, cost in self.adjacentList[currentNode]:
                if distances[neighborNode] > distances[currentNode] + cost:
                    distances[neighborNode] = distances[currentNode] + cost
                    heapq.heappush(minHeap, (distances[neighborNode], neighborNode))
        return distances
    
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # time complexity: O((V + E) * Log(V)) V = 26, E = len(original) which could reach 2000
        # space complexity: O(V + E)
        self.adjacentList = [[] for _ in range(26)] # graph 0 -> 'a', 1 -> 'b' ... 25 -> 'z'
        for i in range(len(original)):
            sourceNodeNumber = ord(original[i]) - ord('a')
            destinationNodeNumber = ord(changed[i]) - ord('a')
            weight = cost[i]
            self.adjacentList[sourceNodeNumber].append((destinationNodeNumber, weight))
        
        costMap = {}
        for nodeNumber in range(26):
            costMap[nodeNumber] = self.dijkstra(nodeNumber)
        
        totalCost = 0
        for i in range(len(source)):
            sourceNodeNumber = ord(source[i]) - ord('a')
            targetNodeNumber = ord(target[i]) - ord('a')
            totalCost += costMap[sourceNodeNumber][targetNodeNumber]
        
        if totalCost == float('inf'):
            totalCost = -1
        return totalCost