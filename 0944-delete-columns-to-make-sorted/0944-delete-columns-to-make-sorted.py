class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        res = 0
        for col in range(m):
            isSorted = True
            for row in range(1, n):
                isSorted &= strs[row - 1][col] <= strs[row][col]
            if isSorted is False:
                res += 1
        return res