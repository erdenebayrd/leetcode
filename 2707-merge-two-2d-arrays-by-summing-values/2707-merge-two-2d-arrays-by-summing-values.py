class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n = 0
        for i in range(len(nums1)):
            n = max(nums1[i][0], n)
        for i in range(len(nums2)):
            n = max(nums2[i][0], n)
        arr = [0] * n
        for i in range(len(nums1)):
            arr[nums1[i][0] - 1] += nums1[i][1]
        for i in range(len(nums2)):
            arr[nums2[i][0] - 1] += nums2[i][1]
        res = []
        for i in range(n):
            if arr[i] > 0:
                res.append([i + 1, arr[i]])
        return res