class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # time: O(m * (k + n)) # m = len(patterns), k len(patterns[i]), n = len(word)
        # space: O(k)
        # method: KMP
    
        def kmp(pattern: str, text: str) -> bool:
            n = len(pattern)
            lps = [0] * n
            length = 0
            for i in range(1, n):
                while length > 0 and pattern[length] != pattern[i]:
                    length = lps[length - 1]
                if pattern[length] == pattern[i]:
                    length += 1
                lps[i] = length
            
            length = 0 # matched length
            for ch in text:
                while length > 0 and pattern[length] != ch:
                    length = lps[length - 1]
                if pattern[length] == ch:
                    length += 1
                if length == n:
                    return True
            return False
    
        count = 0
        for pattern in patterns:
            if kmp(pattern, word):
                count += 1
        return count