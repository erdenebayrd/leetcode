class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # # time: O(log2(N) + log3(N) + ... log(N-2)(N))
        # # space: O(log2(N) + log3(N) + ... log(N-2)(N))
        # # method: simulation

        # def convertToBase(number: int, base: int) -> str:
        #     result = ""
        #     while number:
        #         digit = number % base
        #         result += str(digit)
        #         number //= base
        #     result = result[::-1]
        #     return result
        
        # def isPalindrome(text: str) -> bool:
        #     n = len(text)
        #     for i in range(n//2):
        #         if text[i] != text[n - 1 - i]:
        #             return False
        #     return True
        
        # for base in range(2, n - 1):
        #     baseNumber = convertToBase(n, base)
        #     if isPalindrome(baseNumber) is False:
        #         return False
        # return True

        """
            since any number greater than 4's base n - 2 number is alwas 12 which is not palindrome
            and 4's base 2 is 10 which is not palindromic
            basically there is no strictly palindromic number
        """
        return False