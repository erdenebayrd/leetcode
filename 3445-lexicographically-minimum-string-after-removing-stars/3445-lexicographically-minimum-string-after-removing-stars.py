class Solution:
    def clearStars(self, s: str) -> str:
        pq = []
        for idx, ch in enumerate(s):
            if ch == "*":
                heapq.heappop(pq)
            else:
                heapq.heappush(pq, (ch, -idx))
        
        res = []
        while pq:
            ch, idx = heapq.heappop(pq)
            res.append((-idx, ch))
        res.sort()
        return "".join([ch for idx, ch in res])