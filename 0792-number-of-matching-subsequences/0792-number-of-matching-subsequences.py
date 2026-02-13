from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        charIndexes = defaultdict(list)
        for i in range(len(s)):
            charIndexes[s[i]].append(i)
        
        def found(word: str) -> bool: # O(M * Log N) M is the length of word given as param, N is the length of string s
            lastIndex = -1
            for character in word:
                low, high = -1, len(charIndexes[character])
                while low + 1 < high:
                    middle = (low + high) // 2
                    if lastIndex < charIndexes[character][middle]:
                        high = middle
                    else:
                        low = middle
                if high == len(charIndexes[character]):
                    return False
                lastIndex = charIndexes[character][high]
            return True


        result = 0
        for word in words:
            if found(word):
                result += 1
        
        return result