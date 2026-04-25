class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # time: O(log2(N) + log3(N) + ... log(N-2)(N))
        # space: O(log2(N) + log3(N) + ... log(N-2)(N))
        # method: simulation

        def convertToBase(number: int, base: int) -> str:
            result = ""
            while number:
                digit = number % base
                result += str(digit)
                number //= base
            result = result[::-1]
            return result
        
        def isPalindrome(text: str) -> bool:
            n = len(text)
            for i in range(n//2):
                if text[i] != text[n - 1 - i]:
                    return False
            return True
        
        for base in range(2, n - 1):
            if isPalindrome(convertToBase(n, base)) is False:
                return False
        return True