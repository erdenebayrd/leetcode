import bisect
from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def calculateDifference(value: int, nums: List[int]) -> int: # O(N)
            total = 0
            for num in nums:
                if num > value:
                    total += value
                else:
                    total += num
            return abs(total - target)
        
        lo, hi = -1, target + 1
        while lo + 1 < hi:
            md = (lo + hi) // 2
            if calculateDifference(md, arr) <= calculateDifference(md + 1, arr):
                hi = md
            else:
                lo = md
        return hi