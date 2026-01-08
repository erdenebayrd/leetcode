class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # time: O(N * M)
        # space: O(N * M)
        n = len(nums1)
        m = len(nums2)
        
        @cache
        def solve(i: int, j: int) -> int:
            if i >= n or j >= m:
                return 0
            # Options
            # 1. Choose both i, j
            res = nums1[i] * nums2[j] + solve(i + 1, j + 1)
            # 2. Skip i
            res = max(res, solve(i + 1, j))
            # 3. Skip j
            res = max(res, solve(i, j + 1))
            return res
        
        res = -int(5e8 + 1)
        for i in range(n):
            for j in range(m):
                res = max(res, nums1[i] * nums2[j] + solve(i + 1, j + 1))
        return res