class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # time: O(N * LogN)
        # space: O(N)
        # method: dijkstra with double graph (cost)
        inf = int(2e9)
        n = len(moveTime)
        m = len(moveTime[0])
        cost = [[[inf] * 2 for _ in range(m)] for _ in range(n)]
        cost[0][0][1] = 0
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        moveTime[0][0] = 0
        
        pq = [(cost[0][0][1], 0, 0, 1)]
        heapq.heapify(pq)
        while len(pq) > 0:
            _, x, y, preState = heapq.heappop(pq)
            curState = preState ^ 1
            for i in range(4):
                curx = dx[i] + x
                cury = dy[i] + y
                if curx < 0 or curx >= n or cury < 0 or cury >= m:
                    continue
                curCost = max(cost[x][y][preState], moveTime[curx][cury]) + curState + 1
                if cost[curx][cury][curState] > curCost:
                    cost[curx][cury][curState] = curCost
                    heapq.heappush(pq, (cost[curx][cury][curState], curx, cury, curState))
        # print(cost)
        return min(cost[n - 1][m - 1])
