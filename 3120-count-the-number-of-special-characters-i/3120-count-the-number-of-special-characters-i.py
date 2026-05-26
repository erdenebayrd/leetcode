class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # time: O(N) N is the number of characters in word
        # space: O(1)
        # method: bitmask since the total unique chars are limited to 52 at most
        lower_bitmask = upper_bitmask = 0
        for ch in word:
            if 'a' <= ch <= 'z': # lower
                value = ord(ch) - ord('a')
                lower_bitmask |= 1 << value
            else: # upper
                value = ord(ch) - ord('A')
                upper_bitmask |= 1 << value
        bitmask = lower_bitmask & upper_bitmask
        count_specials = bitmask.bit_count()
        return count_specials