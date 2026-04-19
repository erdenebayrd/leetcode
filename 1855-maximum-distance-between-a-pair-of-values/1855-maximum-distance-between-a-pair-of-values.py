class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # time: O(N log M)
        # space: O(1)
        # method: binary search
        result = 0
        n = len(nums1)
        m = len(nums2)
        # for i in range(n):
        #     low, high = i - 1, m
        #     while low + 1 < high:
        #         mid = (low + high) // 2
        #         if nums1[i] <= nums2[mid]:
        #             low = mid
        #         else:
        #             high = mid
        #     if low == i - 1:
        #         continue
        #     result = max(result, low - i)
        # return result

        # time: O(N + M)
        # space: O(1)
        # method: 2 pointers
        j = 0
        for i in range(n):
            j = max(j, i)
            while j < m and nums1[i] <= nums2[j]:
                j += 1
            result = max(result, j - i - 1)
        return result