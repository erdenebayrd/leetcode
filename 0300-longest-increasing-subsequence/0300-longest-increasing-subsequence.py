class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        subArray = [nums[0]]
        for i in range(1, n):
            if subArray[-1] < nums[i]:
                subArray.append(nums[i])
            else:
                lo, hi = -1, len(subArray)
                while lo + 1 < hi:
                    md = (lo + hi) // 2
                    if nums[i] <= subArray[md]:
                        hi = md
                    else:
                        lo = md
                subArray[hi] = nums[i]
        return len(subArray)