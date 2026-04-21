class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(N)
        # method: prefix sum
        n = len(nums)
        prefix = [0] * n
        for i in range(n):
            value = nums[i]
            if value == 0:
                value = -1
            prefix[i] += value + prefix[i - 1]
        result = 0
        seen = {0: -1}
        for i in range(n):
            need = prefix[i]
            if need in seen:
                result = max(result, i - seen[need])
            if prefix[i] not in seen:
                seen[prefix[i]] = i
        return result