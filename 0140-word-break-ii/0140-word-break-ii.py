from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # -------------------------------------- recursive --------------------------------------
        # time: O(N * 2 ^ N)
        # space: O(N * 2 ^ N)
        # words = defaultdict(bool)
        # for word in wordDict:
        #     words[word] = True
        
        # s = "a_a_a_a_a_a_a_a" n - 1 gaps between a's, we have 2 choices in every gap, choose/split it or not use it.
        #.      1.0 0.0.1.0.0 2 ^ (n - 1)
        #      aa aaa aa aaa
        # wordDict = [a, aa, aaa, aaaa, aaaaa]

        # result = []
        # currentBreaks = []

        # def breakWord(left: int) -> None:
        #     if left == len(s):
        #         result.append(" ".join(currentBreaks))
        #         return
        #     for right in range(left, len(s)):
        #         word = s[left:right + 1]
        #         if word in words:
        #             currentBreaks.append(word)
        #             breakWord(right + 1)
        #             currentBreaks.pop()
        
        # breakWord(0)
        # return result

        # -------------------------------------- bitmask --------------------------------------
        # time: O(n * 2 ^ n)
        # space: O(n * 2 ^ n)
        words = defaultdict(bool)
        for word in wordDict:
            words[word] = True
        
        result = []
        n = len(s)
        for bitmask in range(1 << (n - 1)): # O(2 ^ (n-1))
            currentResult = []
            left = 0
            # "catsanddog"
            #  000000001 => "catsanddo" "g"
            for index in range(n - 1): # if index'th bit is 1, we would use the split between index and index + 1'th character O(n)
                if bitmask & (1 << index): # means, at index'th bit is 1
                    currentResult.append(s[left:index + 1])
                    left = index + 1
            currentResult.append(s[left:n])
            # check all the substring in currentResult is contained in the hashMap "words"
            isCurrentResultContained = True
            for word in currentResult:
                isCurrentResultContained &= (word in words)
            if isCurrentResultContained is True:
                result.append(" ".join(currentResult))
        return result