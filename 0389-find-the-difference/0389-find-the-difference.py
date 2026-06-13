class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        number = 0
        for ch in s:
            number ^= ord(ch)
        for ch in t:
            number ^= ord(ch)
        return chr(number)
        