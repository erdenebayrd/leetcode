from collections import defaultdict, deque

class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        """
            graph problem
            if there is a cycle, not possible to finish all courses
            we can determine graph cycle using Kahn's algorithm
            which works by 
                "*" building adjacent list 
                "*" counting graph input degrees
                "*" start from nodes with 0 input degree
                "*" visiting neighbors then decreasing degree of neighbors by 1 if the neighbors input degree become 0, add it to the queue
                "*" after all check input degrees of all nodes if there is a node with input degree more than 0, there must be cycle

            while detecting cycle by Kahn's algo we can do following to trace path
                "*" order of nodes in the queue would be stored as paths in other variable
                "*" if there is no cycle, we can just return the variable paths
            
            time complexity would be O(V + E) V is total number of nodes/vertices, E is total number of edges between nodes
            space complexity would be O(V + E)
        """
        # time: O(V + E)
        # space: O(V + E)
        # method: graph Kahn's algorithm
        adjacent_list = defaultdict(list)
        in_degree = defaultdict(int)
        for u, v in prerequisites:
            adjacent_list[v].append(u)
            in_degree[u] += 1
        
        queue = deque()
        for node in range(num_courses):
            if in_degree[node] == 0:
                queue.append(node)
        
        paths = []
        while queue:
            node = queue.popleft()
            paths.append(node)
            for neighbor in adjacent_list[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        for node in range(num_courses):
            if in_degree[node] > 0:
                return []
        return paths