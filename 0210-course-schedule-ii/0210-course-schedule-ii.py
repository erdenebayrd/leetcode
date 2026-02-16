from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # numCourses = 6
        # --------------
        # 1 <- 0
        # |    |
        # V    V
        # 3 <- 2

        # 4 -> 5

        # can be: 0 -> 4 -> 5 -> 1 -> 2 -> 3 
        indegree = defaultdict(int)
        graph = defaultdict(list)
        for nodeU, nodeV in prerequisites:
            graph[nodeV].append(nodeU)
            indegree[nodeU] += 1
        
        queue = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)
        
        topological = []
        while queue:
            node = queue.popleft()
            topological.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        for node in range(numCourses):
            if indegree[node] > 0:
                return []
        return topological