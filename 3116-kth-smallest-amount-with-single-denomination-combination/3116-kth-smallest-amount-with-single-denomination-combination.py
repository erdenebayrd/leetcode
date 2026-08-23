import math

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # time: O(n * 2 ^ n * log(max(coins) * k) * log(max(coins)) ) n = len(coins)
        # space: O(1)
        # method: math lcm

        n = len(coins)
        def count_lower_or_equal(candidate: int) -> int:
            count = 0
            for bitmask in range(1, 1 << n):
                lcm = 1
                bit_count = bitmask.bit_count() # O(1)
                while bitmask: # log(bitmask)
                    bit = bitmask & -bitmask
                    bitmask -= bit
                    lcm = math.lcm(lcm, coins[bit.bit_length() - 1])
                
                count += (candidate // lcm) * (((bit_count & 1) << 1) - 1)
                
            return count

        low, high = 0, k * max(coins) + 1
        while low + 1 < high:
            mid = (low + high) // 2
            if count_lower_or_equal(mid) < k:
                low = mid
            else:
                high = mid
        return high