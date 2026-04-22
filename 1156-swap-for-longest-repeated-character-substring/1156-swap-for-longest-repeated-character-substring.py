from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        """
        so we can at most 1 swap and need to get longest continuous substring with same characters
        I can prepare prefix and suffix sum of each character that appear consecutively
        for example:
        
        prefix would be like below
                  V
            0 1 2 3 4 5 6
            a a a b a a a
        a:  1 2 3 0 1 2 3
        b:  0 0 0 1 0 0 0
        c:  0 0 0 .......
        ..   ...
        z:  0 0 0 
        """
        # time: O(26 * N)
        # space: O(26 * N)
        # method: prefix/suffix sum, counting
        total = Counter(text)
        # print(total)
        n = len(text)
        prefix = [[0] * n for _ in range(26)]
        suffix = [[0] * n for _ in range(26)]
        prefix[ord(text[0]) - ord('a')][0] = 1
        for i in range(1, n):
            character = ord(text[i]) - ord('a')
            prefix[character][i] += prefix[character][i - 1] + 1

        suffix[ord(text[-1]) - ord('a')][-1] = 1
        for i in range(n - 2, -1, -1):
            character = ord(text[i]) - ord('a')
            suffix[character][i] += suffix[character][i + 1] + 1
        # print(prefix)
        # print(suffix)
        def getPrefixSum(character: int, index: int) -> int:
            if index < 0 or index >= n:
                return 0
            return prefix[character][index]

        def getSuffixSum(character: int, index: int) -> int:
            if index < 0 or index >= n:
                return 0
            return suffix[character][index]

        result = 0
        for character in range(26):
            for index in range(n):
                left = getPrefixSum(character, index - 1)
                right = getSuffixSum(character, index + 1)
                # print(left, right, total[character])
                if total[chr(character + ord('a'))] > left + right: # we can swap
                    result = max(result, left + right + 1)
                elif total[chr(character + ord('a'))] == left + right: # we can swap
                    result = max(result, left + right)
        return result