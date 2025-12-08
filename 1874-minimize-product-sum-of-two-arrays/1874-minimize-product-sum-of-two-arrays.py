class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        cnt1 = [0] * 101
        cnt2 = [0] * 101
        for i in range(n):
            cnt1[nums1[i]] += 1
            cnt2[nums2[i]] += 1
        i = 1
        j = 100
        res = 0
        while i <= 100 and j >= 1:
            while i <= 100 and cnt1[i] == 0:
                i += 1
            while j >= 1 and cnt2[j] == 0:
                j -= 1
            if n > 0:
                res += i * j
                cnt1[i] -= 1
                cnt2[j] -= 1
                n -= 1
        return res