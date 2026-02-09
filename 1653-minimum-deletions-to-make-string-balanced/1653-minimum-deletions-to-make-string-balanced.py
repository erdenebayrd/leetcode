class Solution:
    def minimumDeletions(self, s: str) -> int:
        # time: O(N)
        # space: O(1)
        result = 0
        countB = 0
        for ch in s:
            if ch == 'a':
                result = min(result + 1, countB) # means delete all occurrences of "b" before this character OR delete this character "a" then go to next
            else: # b
                countB += 1
        return result