class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        for word in text.split(" "):
            if any(ch in word for ch in brokenLetters):
                continue
            res += 1
        return res