class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        streak = 1
        count = Counter(nums)
        res = max(1, 1 + ((count[1] - 1) // 2) * 2)
        def helper(value: int) -> int:
            x = int(value ** 0.5)
            if x * x == value and count[x] >= 2:
                return 1 + helper(x)
            return 0

        for num in nums:
            if num == 1:
                continue
            res = max(res, 1 + 2 * helper(num))
        return res