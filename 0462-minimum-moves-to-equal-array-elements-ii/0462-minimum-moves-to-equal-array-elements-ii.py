class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # time: O(N * log (maxValue - minValue))
        # space: O(1)
        # method: ternary search
        n = len(nums)

        def cost(value: int) -> int:
            result = 0
            for number in nums:
                result += abs(number - value)
            return result

        low, high = min(nums) - 1, max(nums) + 1
        while low + 1 < high:
            mid = (low + high) // 2
            if cost(mid) < cost(mid + 1):
                high = mid
            else: # cost(mid) >= cost(mid + 1):
                low = mid
        return cost(high)