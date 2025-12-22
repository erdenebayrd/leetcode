class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        inf = int(2e6)

        def countStrictlyLowerElements(x: int) -> int:
            res = bisect_left(nums1, x) 
            res += bisect_left(nums2, x)
            return res
        
        def countExactlyEqualElements(x: int) -> int:
            res = bisect_right(nums1, x) - bisect_left(nums1, x)
            res += bisect_right(nums2, x) - bisect_left(nums2, x)
            return res

        def countStrictlyGreaterElements(x: int) -> int:
            res = countStrictlyLowerElements(x)
            res += countExactlyEqualElements(x)
            res = n + m - res
            return res

        def binSearch(k: int, nums) -> int:
            lo, hi = -1, len(nums)
            while lo + 1 < hi:
                md = (lo + hi) // 2
                x = nums[md]
                lower = countStrictlyLowerElements(x)
                equal = countExactlyEqualElements(x)
                higher = countStrictlyGreaterElements(x)
                if lower <= k <= lower + equal - 1:
                    return x
                if k <= lower - 1:
                    hi = md
                else:
                    lo = md
            return inf

        # after concatenating 2 arrays, returns a value of k'th index by O(Log(m + n))
        def findElementByIndex(k: int) -> float:
            res = binSearch(k, nums1)
            if res == inf:
                res = binSearch(k, nums2)
            assert res != inf
            return res

        idx = (n + m) // 2
        if (n + m) & 1:
            return findElementByIndex(idx)
        return (findElementByIndex(idx) + findElementByIndex(idx - 1)) / 2