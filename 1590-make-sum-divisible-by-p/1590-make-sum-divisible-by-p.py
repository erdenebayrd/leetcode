class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # time: O(N)
        # space: O(N)
        # method: prefix sum + math
        n = len(nums)
        total = sum(nums)
        remainder = total % p
        if remainder == 0:
            return 0

        prefix = [0] * n
        prefix[0] = nums[0] % p
        for i in range(1, n):
            prefix[i] = (prefix[i - 1] + nums[i]) % p
        
        position = {0: -1}
        result = n
        for i in range(n):
            need = (prefix[i] - remainder) % p
            if need in position:
                result = min(result, i - position[need])
            position[prefix[i]] = i
        if result == n:
            result = -1
        return result