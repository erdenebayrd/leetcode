class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # time: O(N ^ 3)
        # space: O(N ^ 2)
        
        n = len(strs)
        for i in range(n):
            strs[i] = "a" + strs[i]
        m = len(strs[0])

        @cache
        def solve(le: int, ri: int) -> int:
            if ri >= m:
                return 0
            # Case 1: delete ri'th row
            res = 1 + solve(le, ri + 1) 

            # Case 2: don't delete ri'th row if and only if all rows individualy sorted by lexographic
            # otherwise ri'th row must be deleted and this case is covered by Case 1
            if all([strs[i][le] <= strs[i][ri] for i in range(n)]):
                res = min(res, solve(ri, ri + 1))
            
            return res
        
        res = solve(0, 1)
        solve.cache_clear()
        return res