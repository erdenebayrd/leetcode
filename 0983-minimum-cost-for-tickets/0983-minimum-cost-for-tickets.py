class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        cover = [1, 7, 30]

        @cache
        def solve(idx: int, until: int) -> int:
            if idx >= n:
                return 0
            if days[idx] <= until:
                return solve(idx + 1, until)
            res = int(1e9)
            for i in range(3):
                res = min(res, costs[i] + solve(idx + 1, days[idx] + cover[i] - 1))
            return res
        
        return solve(0, 0)