class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # xor
        # 000010101
        #  000010101
        #----------
        # 000011110
        # 000011111
        # 000100000
        
        if "11" in bin(n):
            return False
        if "00" in bin(n):
            return False
        return True

        xorShift = (n >> 1) ^ n
        result = xorShift & (xorShift + 1) == 0
        return result
        # 000011111111111.   (2 ^ m) - 1
        # 000100000000000.    2 ^ m
        # 000000000000000
        # 1001
        #  100
        #  1101
        # 10000
            