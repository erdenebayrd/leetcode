from functools import cache
from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        words = defaultdict(bool)
        for word in wordDict:
            words[word] = True

        # leet code
        #      ^   
        @cache
        def canBreak(startIndex: int) -> bool:
            if startIndex == len(s):
                return True
            result = False
            currentSubWord = ""
            for index in range(startIndex, len(s)):
                currentSubWord += s[index]
                if currentSubWord in words:
                    result |= canBreak(index + 1)
            return result
        
        # time: O(N ^ 3)
        # space: O(N)
        return canBreak(0)