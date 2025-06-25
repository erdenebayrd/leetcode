class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        lo, hi = -int(1e10 + 1), int(1e10 + 1)
        while lo + 1 < hi:
            md = (lo + hi) // 2
            cntSmallerOrEqual = 0
            for num in nums1:
                cnt = 0
                if md < 0:
                    if num < 0:
                        x = md / num
                        cnt += len(nums2) - bisect.bisect_left(nums2, x)
                    elif num == 0:
                        pass # nothing to do
                    else: # num > 0
                        x = md / num
                        cnt += bisect.bisect_right(nums2, x)
                elif md == 0:
                    if num < 0:
                        cnt += len(nums2) - bisect.bisect_left(nums2, 0)
                    elif num == 0:
                        cnt += len(nums2)
                    else: # num > 0
                        cnt += bisect.bisect_right(nums2, 0)
                else: # md > 0
                    if num < 0:
                        x = md / num
                        cnt += len(nums2) - bisect.bisect_left(nums2, x)
                    elif num == 0:
                        cnt += len(nums2)
                    else: # num > 0
                        x = md / num
                        cnt += bisect.bisect_right(nums2, x)
                cntSmallerOrEqual += cnt
            if cntSmallerOrEqual >= k:
                hi = md
            else: # cntSmallerOrEqual < k
                lo = md
        return hi