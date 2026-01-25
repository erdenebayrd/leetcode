class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        for i in range(n + m - 1, n - 1, -1):
            nums1[i] = nums1[i - n]
        # print(nums1)
        i = n
        j = 0
        idx = 0
        while j < n and i < n + m:
            if nums1[i] < nums2[j]:
                nums1[idx] = nums1[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
            idx += 1
        while j < n:
            nums1[idx] = nums2[j]
            idx += 1
            j += 1
        while i < n + m:
            nums1[idx] = nums1[i]
            idx += 1
            i += 1