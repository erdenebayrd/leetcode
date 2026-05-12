from functools import lru_cache

class Solution:
    def stoneGameV(self, stone_values: List[int]) -> int:
        # time: O(N ^ 3)
        # space: O(N ^ 2)
        # method: DP

        n = len(stone_values)

        @lru_cache(None)
        def solve(left: int, right: int) -> int:
            if left >= right:
                return 0
            
            result = 0
            left_sum = 0
            total = sum(stone_values[left: right + 1])
            for i in range(left, right):
                left_sum += stone_values[i]
                right_sum = total - left_sum
                if left_sum < right_sum:
                    result = max(result, left_sum + solve(left, i))
                elif left_sum > right_sum:
                    result = max(result, right_sum + solve(i + 1, right))
                else: # left_sum == right_sum
                    result = max(result, left_sum + max(solve(left, i), solve(i + 1, right)))
            return result
        
        return solve(0, n - 1)