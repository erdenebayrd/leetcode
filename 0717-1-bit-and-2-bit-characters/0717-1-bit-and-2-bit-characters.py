class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        idx = 0
        while idx < n - 1:
            if bits[idx] == 1:
                idx += 1
            idx += 1
        return idx == n - 1