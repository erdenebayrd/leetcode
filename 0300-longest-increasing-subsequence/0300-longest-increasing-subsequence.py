class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        subArray = [nums[0]]
        for i in range(1, n):
            if subArray[-1] < nums[i]:
                subArray.append(nums[i])
            else:
                for j in range(len(subArray)):
                    if nums[i] <= subArray[j]:
                        subArray[j] = nums[i]
                        break
        return len(subArray)