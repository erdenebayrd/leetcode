from typing import List
from collections import defaultdict

class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        # time: O(N)
        # space: O(N)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        distance = [[0] * n for _ in range(3)]
        # time: O(N)
        def calculateDistance(parent: int, node: int, fromNode: int, currentDistance: int): # fromNode = 1 means x, 2 means y, 3 means z
            distance[fromNode][node] = currentDistance
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                calculateDistance(node, neighbor, fromNode, currentDistance + 1)
        
        nodes = [x, y, z]
        for i in range(len(nodes)):
            calculateDistance(-1, nodes[i], i, 0)
        
        def isPythagoreanTriplet(triplet: List[int]) -> bool:
            triplet.sort()
            return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2
        
        result = 0
        for node in range(n):
            if isPythagoreanTriplet([distance[fromNode][node] for fromNode in range(len(nodes))]):
                result += 1
        return result