class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        for word in words:
            count = 0
            for ch in word:
                count += weights[ord(ch) - ord("a")]
            count %= 26
            count = 25 - count
            result.append(chr(ord("a") + count))
        return "".join(result)