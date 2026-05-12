from functools import lru_cache

class Solution:
    def stoneGameIII(self, stone_values: List[int]) -> str:
        # time: O(N)
        # space: O(N)
        # method: DP

        n = len(stone_values)
        prefix = [0] * n
        prefix[0] = stone_values[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stone_values[i]
        
        def get_range_sum(left: int, right: int) -> int:
            if left > right:
                return 0
            if left == 0:
                return prefix[right]
            return prefix[right] - prefix[left - 1]

        total = prefix[-1]

        @lru_cache(None)
        def solve(index: int) -> int:
            if index >= n:
                return 0
            
            result = float('-inf')
            cumulative_sum = 0
            for i in range(index, min(index + 3, n)):
                cumulative_sum += stone_values[i]
                result = max(result, cumulative_sum + get_range_sum(i + 1, n - 1) - solve(i + 1))
            return result
        
        alice = solve(0)
        bob = total - alice
        if alice > bob:
            return "Alice"
        elif alice < bob:
            return "Bob"
        return "Tie"