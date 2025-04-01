class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        adj = defaultdict(list)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        n, m = len(grid), len(grid[0])
        # print(n, m)
        nodeMapReverse = defaultdict(tuple)
        nodeMap = [[0] * m for _ in range(n)]
        # print("-" * 10)
        for i in range(n):
            for j in range(m):
                # print(i * m + j)
                nodeMap[i][j] = i * m + j
                nodeMapReverse[i * m + j] = (i, j)
        # print("-" * 10)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    for k in range(4):
                        x = dx[k] + i
                        y = dy[k] + j
                        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 2:
                            continue
                        # adj[nodeMap[i][j]].append(nodeMap[x][y])
                        # if grid[x][y] == 1:
                        #     continue
                        # adj[nodeMap[x][y]].append(nodeMap[i][j])
                        adj[nodeMap[x][y]].append(nodeMap[i][j])
                        if grid[x][y] == 1:
                            continue
                        adj[nodeMap[i][j]].append(nodeMap[x][y])
        
        # print(nodeMapReverse)
        def dijkstra(nodeNum: int) -> List[int]:
            dist = [int(1e9)] * n * m
            dist[nodeNum] = 0
            minHeap = []
            heapq.heappush(minHeap, (dist[nodeNum], nodeNum))
            while minHeap:
                _, curNode = heapq.heappop(minHeap)
                for ch in adj[curNode]:
                    if dist[ch] > dist[curNode] + 1:
                        dist[ch] = dist[curNode] + 1
                        heapq.heappush(minHeap, (dist[ch], ch))
            return dist
        
        def bfs(nodeNum: int) -> List[int]:
            dist = [int(1e9)] * n * m
            vis = [False] * n * m
            dist[nodeNum] = 0
            vis[nodeNum] = True
            queue = deque()
            queue.append(nodeNum)
            while queue:
                curNode = queue.popleft()
                for ch in adj[curNode]:
                    if vis[ch] is True:
                        continue
                    vis[ch] = True
                    queue.append(ch)
                    dist[ch] = dist[curNode] + 1
            return dist
        
        res = int(1e9)
        distance = defaultdict(int)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # dist = dijkstra(nodeMap[i][j])
                    dist = bfs(nodeMap[i][j])
                    # total = 0
                    for node, cost in enumerate(dist):
                        # print(node, nodeMapReverse[node])
                        x, y = nodeMapReverse[node]
                        if grid[x][y] == 0:
                            # total += cost
                            distance[node] += cost
                    # res = min(res, total)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    res = min(res, distance[nodeMap[i][j]])
        if res == int(1e9):
            res = -1
        return res