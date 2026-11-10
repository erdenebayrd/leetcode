class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * (n + 1)
        for i in range(n):
            if nums[i] == 1:
                prefix[i] += prefix[i - 1] + 1
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                suffix[i] += suffix[i + 1] + 1
        
        result = max(prefix)
        for i in range(n):
            if nums[i] == 0:
                if i - 1 >= 0 and i + 1 < n:
                    result = max(result, 1 + suffix[i + 1] + prefix[i - 1])
                elif i - 1 >= 0:
                    result = max(result, 1 + prefix[i - 1])
                elif i + 1 < n:
                    result = max(result, 1 + suffix[i + 1])
                else:
                    result = max(result, 1)
        return result