class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # xor
        # 000010101
        #  000010101
        #----------
        # 000011110
        # 000011111
        # 000100000
        
        xorValue = n ^ (n >> 1)
        return xorValue & (xorValue + 1) == 0