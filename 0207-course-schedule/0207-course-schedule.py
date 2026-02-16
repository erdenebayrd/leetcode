from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for nodeU, nodeV in prerequisites:
            graph[nodeU].append(nodeV)
            indegree[nodeV] += 1
        
        queue = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.pop()
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        for node in range(numCourses):
            if indegree[node] > 0: # has cycle
                return False
        return True