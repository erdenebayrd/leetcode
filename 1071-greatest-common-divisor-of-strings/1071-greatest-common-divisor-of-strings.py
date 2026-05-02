class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # time: O(N ^ 2)
        # space: O(N)
        # method: brute force

        if len(str1) > len(str2):
            str1, str2 = str2, str1
        
        def match(gcd: str, text: str) -> bool:
            if len(text) % len(gcd) != 0:
                return False
            times = len(text) // len(gcd)
            return gcd * times == text
        
        result = ""
        prefix = ""
        for ch in str1:
            prefix += ch
            if match(prefix, str1) and match(prefix, str2):
                result = prefix
        return result