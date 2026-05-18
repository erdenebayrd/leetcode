from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        if I do regular dfs or bfs to check every edge, it will lead to TLE
        as number of edges can be N ^ 2. 

        based on the idea below we can greedily solve
            * group every node by it's value
            * starting from 0'th index and iterate it's all children, after iterating all children, we should change graph by deleting childrens already visited
            * so that, we can only visit each node by one and deleting it's edges after visiting the nodes.
        """
        graph = defaultdict(list)
        n = len(arr)
        for i in range(n):
            graph[arr[i]].append(i)
        
        queue = deque()
        queue.append((0, 0)) # the starting index
        visited = set()
        visited.add(0)

        while queue:
            node, cost = queue.popleft()

            if node == n - 1:
                return cost

            # iterating all childrens
            for neighbor in graph[arr[node]]:
                if neighbor not in visited:
                    queue.append((neighbor, cost + 1))
                    visited.add(neighbor)

            del graph[arr[node]]
            if node - 1 >= 0 and node - 1 not in visited:
                visited.add(node - 1)
                queue.append((node - 1, cost + 1))
            if node + 1 < n and node + 1 not in visited:
                visited.add(node + 1)
                queue.append((node + 1, cost + 1))
        
        return -1