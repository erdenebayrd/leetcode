class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # time: O(N)
        # space: O(N)
        # method: prefix sum + hashmap

        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] += prefix[i - 1] + nums[i]

        hashmap = {}
        result = float('-inf')
        for i in range(n):
            if nums[i] - k in hashmap:
                result = max(result, prefix[i] - hashmap[nums[i] - k])
            if nums[i] + k in hashmap:
                result = max(result, prefix[i] - hashmap[nums[i] + k])
            
            if nums[i] not in hashmap:
                hashmap[nums[i]] = float('inf')
            
            value = prefix[i - 1] if i - 1 >= 0 else 0
            hashmap[nums[i]] = min(hashmap[nums[i]], value)

        if result == float('-inf'):
            result = 0
        return result