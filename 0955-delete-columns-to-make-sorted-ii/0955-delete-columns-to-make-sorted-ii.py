class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[-1])
        cur = [""] * n
        
        def isSorted() -> bool:
            return all([cur[i] <= cur[i + 1] for i in range(n - 1)])
        
        def addCol(col: int):
            for i in range(n):
                cur[i] += strs[i][col]
        
        def removeLatestColumn():
            for i in range(n):
                cur[i] = cur[i][:-1]
        
        res = 0
        for i in range(m):
            addCol(i)
            if isSorted() is False:
                removeLatestColumn()
                res += 1
        return res