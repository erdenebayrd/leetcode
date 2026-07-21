class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # time: O(N)
        # space: O(1)
        # method: counting
        result = prev_zeros = current_ones = next_zeros = count = 0
        for ch in s:
            if ch == '0':
                if current_ones == 0:
                    prev_zeros += 1
                else:
                    next_zeros += 1
            else:
                count += 1
                if next_zeros > 0:
                    result = max(result, prev_zeros + next_zeros)
                    prev_zeros = next_zeros
                    current_ones = next_zeros = 0
                
                if prev_zeros > 0 and next_zeros == 0:
                    current_ones += 1

        if next_zeros > 0:
            result = max(result, prev_zeros + next_zeros)
        result += count
        return result