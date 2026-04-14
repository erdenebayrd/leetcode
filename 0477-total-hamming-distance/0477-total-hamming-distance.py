class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # time: O(N log M)
        # space: O(1)
        # method: count
        result = 0
        n = len(nums)
        bits = max(nums).bit_length()
        """
        4:    0100
        14:   1110
        2:    0010
        """
        for _ in range(bits):
            ones = 0
            zeros = 0
            for i in range(n):
                if nums[i] & 1:
                    ones += 1
                else:
                    zeros += 1
                nums[i] >>= 1
            result += ones * zeros
        return result