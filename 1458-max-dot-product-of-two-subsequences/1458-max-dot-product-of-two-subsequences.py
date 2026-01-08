class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # time: O(N * M)
        # space: O(N * M)
        n = len(nums1)
        m = len(nums2)
        
        @cache
        def solve(i: int, j: int) -> int:
            if i >= n or j >= m:
                return -int(5e8 + 1)
            # Options
            # 1. Choose both i, j
            res = nums1[i] * nums2[j] + solve(i + 1, j + 1)
            # 2. Skip i
            res = max(res, solve(i + 1, j))
            # 3. Skip j
            res = max(res, solve(i, j + 1))
            # 4. Skip both i, j
            res = max(res, nums1[i] * nums2[j])
            return res
        
        return solve(0, 0)