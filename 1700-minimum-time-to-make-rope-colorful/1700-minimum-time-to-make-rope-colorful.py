class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        min_pq = []
        current_color = ""
        n = len(colors)
        
        def solve(idx: int) -> int:
            nonlocal min_pq, res, current_color
            while len(min_pq) > 1:
                res += heapq.heappop(min_pq)
            if idx < 0:
                return
            min_pq = []
            current_color = colors[idx]
            heapq.heappush(min_pq, neededTime[idx])
        
        for i in range(n):
            if current_color == colors[i]:
                heapq.heappush(min_pq, neededTime[i])
            else:
                solve(i)
        solve(-1)
        return res