"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    # def __init__(self) -> None:
    #     self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # time: O(V + E)
        # space: O(V)
        # method: DFS

        # if not node:
        #     return node

        # if node in self.visited:
        #     return self.visited[node]

        # self.visited[node] = Node(node.val, [])
        # for neighbor in node.neighbors:
        #     self.visited[node].neighbors.append(self.cloneGraph(neighbor))

        # return self.visited[node]

        # ------------------------- BFS ------------------------- 
        # time: O(V + E)
        # space: O(V)
        # method: BFS
        
        if not node:
            return node
        
        visited = {}
        queue = deque()
        queue.append(node)
        visited[node] = Node(node.val, [])

        while queue:
            currentNode = queue.popleft()

            for neighbor in currentNode.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = Node(neighbor.val, [])
                visited[currentNode].neighbors.append(visited[neighbor])

        return visited[node]