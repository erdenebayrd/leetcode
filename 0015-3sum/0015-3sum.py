from typing import Tuple

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        seen = set()
        result = set()
        for middle in range(n):
            for right in range(middle + 1, n):
                currentSum = nums[middle] + nums[right]
                need = -currentSum
                if need in seen:
                    candidate = sorted([need, nums[middle], nums[right]])
                    candidateTuple = (candidate[0], candidate[1], candidate[2])
                    if candidateTuple not in result:
                        result.add(candidateTuple)
            seen.add(nums[middle])
        return list(result)