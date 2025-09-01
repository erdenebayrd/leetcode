class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n = len(workers)
        m = len(bikes)
        
        @cache
        def solve(idx: int, pattern: int) -> int:
            if idx >= n:
                return 0
            ret = int(1e18)
            for i in range(m):
                if (pattern >> i) & 1:
                    continue
                dist = abs(bikes[i][0] - workers[idx][0])
                dist += abs(bikes[i][1] - workers[idx][1])
                ret = min(ret, dist + solve(idx + 1, pattern | (1 << i)))
            return ret
        
        return solve(0, 0)