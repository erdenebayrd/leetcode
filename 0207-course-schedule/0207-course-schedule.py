class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)
        state = [0] * numCourses # 0 unvisited, 1 visiting, 2 done

        def hasCycle(currentNode: int) -> bool:
            if state[currentNode] == 1:
                return True
            if state[currentNode] == 2:
                return False
            state[currentNode] = 1
            for neighbor in adj[currentNode]:
                if hasCycle(neighbor):
                    return True
            state[currentNode] = 2
            return False
        
        for course in range(numCourses):
            if state[course] == 0:
                if hasCycle(course) is True:
                    return False
        return True