from collections import defaultdict, deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # time: O(V * 26 + E)
        # space: O(V * 26)
        # method: DFS + Kahn's cycle detection
        n = len(colors)
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                indegree[neighbor] -= 1 # visited from node
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        for i in range(n):
            if indegree[i] > 0: # has cycle
                return -1
        
        count = [[0] * 26 for _ in range(n)]
        visited = [False] * n
        
        def dfs(node: int):
            visited[node] = True
            for neighbor in adj[node]:
                if visited[neighbor] is False:
                    dfs(neighbor)
                for color in range(26):
                    count[node][color] = max(count[node][color], count[neighbor][color])
            color = ord(colors[node]) - ord('a')
            count[node][color] += 1
        
        result = 0
        for i in range(n):
            if visited[i] is True:
                continue
            dfs(i)
            result = max(result, max(count[i]))

        return result