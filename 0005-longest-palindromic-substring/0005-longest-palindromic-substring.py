class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        prefixHash = [0] * n # contains hash value of substring of [0 i'th character] Ex: cbbd => "c * 257 ^ 3 + b * 257 ^ 2 + b * 257 ^ 1 + d * 257 ^ 0"
        suffixHash = [0] * n # similar to prefixHash but from right to left, suffix
        hashBase = 257 # better use big enough base preventing hash collision (ascii of chars are lower than this base)
        mod = 1_000_000_007 # big prime number
        powerBase = [0] * n
        powerBase[0] = 1 # hashBase ^ 0 (257 ^ 0) which is 1 (^ means not bit xor)
        for i in range(1, n):
            powerBase[i] = (powerBase[i - 1] * hashBase) % mod
        
        prefixHash[0] = ord(s[0]) * powerBase[0] # powerBase[0] means 257 ^ 0 = 1
        for i in range(1, n):
            prefixHash[i] = (prefixHash[i - 1] * hashBase + ord(s[i])) % mod # Ex "cb" substring we are at 1'th index which points "b" character. [0: 0] hash -> c * 257 ^ 0. [0, 1] -> (c * 257 ^ 0) * 257 + b = c * 257 ^ 1 + b
        
        suffixHash[n - 1] = ord(s[n - 1])
        for i in range(n - 2, -1, -1):
            suffixHash[i] = (suffixHash[i + 1] * hashBase + ord(s[i])) % mod
        
        def rangeHashPrefix(left: int, right: int) -> int:
            if left == 0:
                return prefixHash[right]
            # Ex: left = 2, right = 3. We do need hash value of "bd" from cbbd => (c * 257 ^ 3 + b * 257 ^ 2 + b * 257 ^ 1 + d * 257 ^ 0) - (c * 257 ^ 1 + b * 257 ^ 0)
            return (prefixHash[right] - (prefixHash[left - 1] * powerBase[right - left + 1]) % mod + mod) % mod
        
        def rangeHashSuffix(left: int, right: int) -> int:
            if right == n - 1:
                return suffixHash[left]
            return (suffixHash[left] - (suffixHash[right + 1] * powerBase[right - left + 1]) % mod + mod) % mod
        
        def isPalindromic(left: int, right: int) -> bool: # time: O(1) doing some math calculation based on rolling hash values
            if left == right:
                return True
            halfLength = (right - left + 1) // 2
            if rangeHashPrefix(left, left + halfLength - 1) == rangeHashSuffix(right - halfLength + 1, right): # [0, 1, 2, 3, 4] halfLength = (4 - 0 + 1) // 2 = 2 --->> prefixHash[0:1] == suffixHash[2:4]
                return True # palindromic substring[left: right + 1]
            return False

        longest = 0
        leftIndex, rightIndex = 0, 0
        
        # longest palindromic substring length is ODD
        for index in range(n): # "index" would be center of palindromic substring
            low, high = 0, min(n - index, index + 1) + 1 # lowest & highest length
            while low + 1 < high: # O(Log N)
                middle = (low + high) // 2
                if isPalindromic(index - middle + 1, index + middle - 1) is True: # first half of substring end at "index", second half of substring starts at "index" both with "middle" length
                    low = middle
                else:
                    high = middle
                currentLength = low + low - 1
                if longest < currentLength:
                    longest = currentLength
                    leftIndex, rightIndex = index - low + 1, index + low - 1

        # longest palindromic substring length is EVEN
        for index in range(n): # first half of string end at "index" and second half starts from "index + 1"
            low, high = 0, min(index + 1, n - index - 1) + 1 # lowest & highest length
            while low + 1 < high: # O(Log N)
                middle = (low + high) // 2
                if isPalindromic(index - middle + 1, index + middle) is True: # first half of substring end at "index", second half of substring starts at "index + 1" both with "middle" length
                    low = middle
                else:
                    high = middle
                currentLength = low + low
                if longest < currentLength:
                    longest = currentLength
                    leftIndex, rightIndex = index - low + 1, index + low

        return s[leftIndex: rightIndex + 1]
