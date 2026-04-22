from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # """
        # so we can at most 1 swap and need to get longest continuous substring with same characters
        # I can prepare prefix and suffix sum of each character that appear consecutively
        # for example:
        
        # prefix would be like below
        #           V
        #     0 1 2 3 4 5 6
        #     a a a b a a a
        # a:  1 2 3 0 1 2 3
        # b:  0 0 0 1 0 0 0
        # c:  0 0 0 .......
        # ..   ...
        # z:  0 0 0 
        # """
        # # time: O(26 * N)
        # # space: O(26 * N)
        # # method: prefix/suffix sum, counting
        # total = Counter(text)
        # # print(total)
        # n = len(text)
        # prefix = [[0] * n for _ in range(26)]
        # suffix = [[0] * n for _ in range(26)]
        # prefix[ord(text[0]) - ord('a')][0] = 1
        # for i in range(1, n):
        #     character = ord(text[i]) - ord('a')
        #     prefix[character][i] += prefix[character][i - 1] + 1

        # suffix[ord(text[-1]) - ord('a')][-1] = 1
        # for i in range(n - 2, -1, -1):
        #     character = ord(text[i]) - ord('a')
        #     suffix[character][i] += suffix[character][i + 1] + 1
        # # print(prefix)
        # # print(suffix)
        # def getPrefixSum(character: int, index: int) -> int:
        #     if index < 0 or index >= n:
        #         return 0
        #     return prefix[character][index]

        # def getSuffixSum(character: int, index: int) -> int:
        #     if index < 0 or index >= n:
        #         return 0
        #     return suffix[character][index]

        # result = 0
        # for character in range(26):
        #     for index in range(n):
        #         left = getPrefixSum(character, index - 1)
        #         right = getSuffixSum(character, index + 1)
        #         # print(left, right, total[character])
        #         if total[chr(character + ord('a'))] > left + right: # we can swap
        #             result = max(result, left + right + 1)
        #         elif total[chr(character + ord('a'))] == left + right: # we can swap
        #             result = max(result, left + right)
        # return result

        """
        we can compress chars by below
        for example:
            aaabaaa
            (a, 3), (b, 1), (a, 3)
        then only need to consider 2 cases
        1. get max count 
        2. if I swap current index if it's count is 1
        """

        # time: O(N)
        # space: O(N)
        # method: compressing
        n = len(text)
        compressed = []
        for i in range(n):
            char = text[i]
            if not compressed or compressed[-1][0] != char:
                compressed.append([char, 1])
            else:
                compressed[-1][1] += 1
        # print(compressed)
        result = 0
        for i in range(len(compressed)):
            result = max(result, compressed[i][1])
        
        total = Counter(text)
        for i in range(1, len(compressed)):
            prevChar, prevCount = compressed[i - 1]
            if total[prevChar] > prevCount:
                result = max(result, prevCount + 1)
        
        for i in range(len(compressed) - 2, -1, -1):
            nextChar, nextCount = compressed[i + 1]
            if total[nextChar] > nextCount:
                result = max(result, nextCount + 1)
        
        for i in range(1, len(compressed) - 1):
            if compressed[i][1] > 1: # checking can we swap or not
                continue
            prevChar, prevCount = compressed[i - 1]
            nextChar, nextCount = compressed[i + 1]
            if prevChar != nextChar:
                continue
            if total[prevChar] == prevCount + nextCount:
                result = max(result, total[nextChar])
            elif total[prevChar] > prevCount + nextCount:
                result = max(result, prevCount + nextCount + 1)
        return result