class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # time: O(k * n * 3)
        # space: O(k * n * 3)
        n = len(prices)
        inf = int(1e12 + 1)

        @cache
        def solve(idx: int, k: int, state: int) -> int:
            if k < 0:
                return -inf
            if idx >= n:
                if state == 0:
                    return 0
                return -inf
            res = solve(idx + 1, k, state)
            if state == 0: # not holding anything
                res = max(res, solve(idx + 1, k - 1, 1) - prices[idx]) # LONG position started at idx
                res = max(res, solve(idx + 1, k - 1, 2) + prices[idx]) # SHORT position started at idx
            elif state == 1: # LONG position started before
                res = max(res, solve(idx + 1, k, 0) + prices[idx]) # closing current LONG position
            elif state == 2: # SHORT position started before
                res = max(res, solve(idx + 1, k, 0) - prices[idx]) # closing current SHORT position
            else:
                assert False
            return res
        
        res = solve(0, k, 0)
        solve.cache_clear()
        return res