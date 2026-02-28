from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        split the pattern into an array
        
        s = aab
        p = c*a*b
        
        first      V
        text =.   [a,  b,  b]
        pattern = [c*, a*, b]
        second     ^

        compare those elements
                ------------------------------------
                first      V
                text =.   [a,  b,  b]
                pattern = [c*, a*, b]
                second         ^
                ------------------------------------
                
                compare the elements

                        ------------------------------------
                        first          V
                        text =.   [a,  b,  b]
                        pattern = [c*, a*, b]
                        second             ^
                        ------------------------------------

                        ------------------------------------
                        first          V
                        text =.   [a,  b,  b]
                        pattern = [c*, a*, b]
                        second         ^
                        ------------------------------------     
        
        DP states would be
        first, second pointer which points text and pattern
        then inside the DP recursive function we use loop to match [0 -> n] characters depending on their character values

        ------------------------------------
        first                 V
        text =.   [a,  b,  b]
        pattern = [.*, a*, b]
        second     ^
        ------------------------------------     

        """

        # time: O(N * M * N) N is len(s), M = len(p), Basically O(N ^ 3)
        # space: O(N * M)
        # method: DP top-down

        text = [ch for ch in s]
        pattern = []
        for ch in p:
            if ch == "*":
                pattern[-1] = pattern[-1] + ch
            else:
                pattern.append(ch)
        
        n = len(text)
        m = len(pattern)

        @cache
        def isMatched(first: int, second: int) -> bool:
            if first == n:
                if second == m:
                    return True
                countAsterisks = 0
                for index in range(second, m):
                    if "*" in pattern[index]:
                        countAsterisks += 1
                if countAsterisks == m - second:
                    return True
                return False
            if second == m:
                return False
            
            result = False
            if "*" in pattern[second]:
                result |= isMatched(first, second + 1) # using zero match of *
                ch = pattern[second][0]
                if ch == "." or ch == text[first]:
                    result |= isMatched(first + 1, second)
                    result |= isMatched(first + 1, second + 1)
            elif "." in pattern[second]:
                result |= isMatched(first + 1, second + 1)
            else:
                if text[first] == pattern[second]:
                    result |= isMatched(first + 1, second + 1)
            return result
        
        return isMatched(0, 0)