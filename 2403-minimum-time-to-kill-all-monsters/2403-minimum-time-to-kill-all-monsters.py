class Solution:
    def minimumTime(self, power: List[int]) -> int:
        # time: O(n * 2 ^ n)
        # space: O(2 ^ n)
        # method: bitmask DP
        n = len(power)
        @cache
        def solve(bitmask: int) -> int:
            killed = bitmask.bit_count()
            if killed == n:
                return 0
            gain = killed + 1
            result = float('inf')
            for i in range(n):
                if bitmask & (1 << i) == 0:
                    days = power[i] // gain + int(power[i] % gain > 0)
                    result = min(result, days + solve(bitmask | (1 << i)))
            return result
        
        return solve(0)