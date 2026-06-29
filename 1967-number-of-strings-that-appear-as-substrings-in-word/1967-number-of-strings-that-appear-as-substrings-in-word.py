class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for pattern in patterns:
            res += int(pattern in word)
        return res