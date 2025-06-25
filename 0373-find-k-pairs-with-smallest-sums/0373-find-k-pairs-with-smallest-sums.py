class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        lo, hi = nums1[0] + nums2[0] - 1, nums1[-1] + nums2[-1] + 1
        while lo + 1 < hi:
            md = (lo + hi) // 2
            cntSmallerOrEqual = 0
            for num in nums1:
                x = md - num
                cnt = bisect.bisect_right(nums2, x)
                cntSmallerOrEqual += cnt
            if cntSmallerOrEqual >= k:
                hi = md
            else:
                lo = md
        res = []
        for x in nums1:
            for y in nums2:
                if x + y >= hi:
                    break
                res.append([x, y])
        for x in nums1:
            ri = bisect.bisect_right(nums2, hi - x)
            le = bisect.bisect_left(nums2, hi - x)
            for i in range(le, ri):
                if len(res) >= k:
                    break
                res.append([x, hi - x])
            if len(res) >= k:
                break
        return res