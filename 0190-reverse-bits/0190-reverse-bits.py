class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for bit in range(32):
            if n & (1 << bit):
                result |= (1 << (31 - bit))
        return result