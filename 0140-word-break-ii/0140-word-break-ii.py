class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # time: O(N ^ 2)
        # space: O(N ^ 2)
        self.words = defaultdict(bool)
        for word in wordDict:
            self.words[word] = True
        
        self.result = []
        self.currentBreaks = []

        def breakWord(left: int) -> None:
            if left == len(s):
                self.result.append(" ".join(self.currentBreaks))
                return
            for right in range(left, len(s)):
                word = s[left:right + 1]
                if word in self.words:
                    self.currentBreaks.append(word)
                    breakWord(right + 1)
                    self.currentBreaks.pop()
        
        breakWord(0)
        return self.result