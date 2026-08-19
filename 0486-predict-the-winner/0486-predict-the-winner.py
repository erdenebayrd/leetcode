class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # time: O(n ^ 2)
        # space: O(n ^ 2)
        # method: DP
        n = len(nums)
        prefix = [0] * n
        dp = [[0] * n for _ in range(n)]
        prefix[0] = nums[0]
        dp[0][0] = nums[0]
        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i - 1]
            dp[i][i] = nums[i]
        
        def get_range_sum(left: int, right: int) -> int:
            if left == 0:
                return prefix[right]
            return prefix[right] - prefix[left - 1]
        
        for size in range(2, n + 1):
            for i in range(size - 1, n):
                left, right = i - size + 1, i
                left_value = nums[left] + get_range_sum(left + 1, right) - dp[left + 1][right]
                right_value = nums[right] + get_range_sum(left, right - 1) - dp[left][right - 1]
                dp[left][right] = max(left_value, right_value)
        return 2 * dp[0][n - 1] >= sum(nums)