class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # time: O(N)
        # space: O(52)
        # method: count
        lower, upper = {}, {}
        lower_bitmask = upper_bitmask = 0
        for i in range(len(word)):
            ch = word[i]
            if 'a' <= ch <= 'z': # lower
                lower[ch] = i
                value = ord(ch) - ord('a')
                lower_bitmask |= (1 << value)
            elif 'A' <= ch <= 'Z' and ch not in upper: # upper
                upper[ch] = i
                value = ord(ch) - ord('A')
                upper_bitmask |= (1 << value)
        
        result = 0
        bitmask = lower_bitmask & upper_bitmask
        while bitmask:
            last_bit = -bitmask & bitmask
            bitmask ^= last_bit
            character_index = last_bit.bit_length() - 1
            lower_char = chr(ord('a') + character_index)
            upper_char = chr(ord('A') + character_index)
            result += int(lower[lower_char] < upper[upper_char])
        return result