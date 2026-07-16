class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = [0] * n
        current_max = nums[0]
        for i in range(n):
            current_max = max(current_max, nums[i])
            prefix_gcd[i] = gcd(current_max, nums[i])
        prefix_gcd.sort()
        result = 0
        for i in range(n // 2):
            result += gcd(prefix_gcd[i], prefix_gcd[n - 1 - i])
        return result