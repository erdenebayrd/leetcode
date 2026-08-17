class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # time: O(N * M)
        # space: O(M)
        # method: bottom-up DP
        n = len(nums1)
        m = len(nums2)
        prev = [0] * m
        for i in range(m):
            prev[i] = int(nums1[0] == nums2[i])
        
        result = max(prev)
        for i in range(1, n):
            curr = [0] * m
            if nums1[i] == nums2[0]:
                curr[0] = 1
            for j in range(1, m):
                if nums1[i] == nums2[j]:
                    curr[j] = prev[j - 1] + 1
            result = max(result, max(curr))
            prev = curr

        return result