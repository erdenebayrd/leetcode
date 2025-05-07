class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # time: O(N * M * Log(N * M))
        # space: O(N * M)
        # method: dijkstra
        n = len(moveTime)
        m = len(moveTime[0])

        def coordinateToNodeNum(x: int, y: int) -> int:
            return x * m + y
        
        def nodeNumToCoordinate(x: int) -> List[int]:
            return [x // m, x % m]
        
        cost = [[int(2e9)] * m for _ in range(n)]
        cost[0][0] = 0
        moveTime[0][0] = 0
        
        pq = [[cost[0][0], 0]]
        heapq.heapify(pq)
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while len(pq) > 0:
            _, node = heapq.heappop(pq)
            x, y = nodeNumToCoordinate(node)
            # print(node, x, y, _)
            for i in range(4):
                curx = dx[i] + x
                cury = dy[i] + y
                if curx < 0 or curx >= n or cury < 0 or cury >= m:
                    continue
                # print("-" * 10)
                # print(curx, cury)
                # print(x, y)
                # print("-" * 10)
                curCost = max(moveTime[curx][cury], cost[x][y]) + 1
                if cost[curx][cury] > curCost:
                    cost[curx][cury] = curCost
                    # if x == 0 and y == 0:
                    #     print((cost[curx][cury], coordinateToNodeNum(curx, cury)))
                    heapq.heappush(pq, [cost[curx][cury], coordinateToNodeNum(curx, cury)])
        # for i in range(n):
        #     print(cost[i])
        return cost[n - 1][m - 1]