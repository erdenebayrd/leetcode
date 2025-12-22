class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # time: O(M * M * N) -> O(N^3)
        # space: O(N ^ 3)
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
            if all([strs[i][le] <= strs[i][ri] for i in range(n)]):
                res = min(res, solve(ri, ri + 1))
            
            return res
        
        return solve(0, 1)