class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # tc: O(N)
        # sc: O(N)

        n = len(nums)
        existed = [False] * (n + 1)

        for i in range(n):
            if 1 <= nums[i] <= n:
                existed[nums[i]] = True
        for i in range(1, n + 1):
            if existed[i] is False:
                return i
        return n + 1