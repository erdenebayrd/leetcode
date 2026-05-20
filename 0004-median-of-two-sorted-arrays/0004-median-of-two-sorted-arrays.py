import bisect
from typing import Optional

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:                
        # time: O(log(n) * log(m))
        # space: O(1)
        # method: binary search

        def count_less(value: int, strictly: bool) -> int:
            if strictly:
                return bisect.bisect_left(nums1, value) + bisect.bisect_left(nums2, value)
            return bisect.bisect_right(nums1, value) + bisect.bisect_right(nums2, value)

        def binary_search(k: int, nums: List[int]) -> Optional[int]:
            low, high = -1, len(nums)
            while low + 1 < high:
                mid = (low + high) // 2
                value = nums[mid]
                less_count = count_less(value, True)
                less_equal_count = count_less(value, False)
                if less_count <= k < less_equal_count:
                    return value
                elif k < less_count:
                    high = mid
                else:
                    low = mid
            return None

        def find_kth_value(k: int) -> int:
            # start searching from nums1
            value = binary_search(k, nums1)
            if value is not None:
                return value
            value = binary_search(k, nums2)
            return value
        
        n = len(nums1) + len(nums2)
        mid_index = (n - 1) // 2
        median = find_kth_value(mid_index)
        if n & 1 == 0: # even length
            median += find_kth_value(mid_index + 1)
            median /= 2
        return median