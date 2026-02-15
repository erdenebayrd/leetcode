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
            for index in range(startIndex, len(s)):
                if s[startIndex:index + 1] in words:
                    result |= canBreak(index + 1)
            return result
        
        # time: O(N ^ 2)
        # space: O(N)
        return canBreak(0)