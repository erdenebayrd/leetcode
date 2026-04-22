class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # time: O(N)
        # space: O(N)
        # method: DP
        count = defaultdict(int)
        count[0] = 1
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        
        result = 0
        for i in range(n):
            # prefix[i] - x == goal
            need = prefix[i] - goal
            result += count[need]
            count[prefix[i]] += 1
        return result