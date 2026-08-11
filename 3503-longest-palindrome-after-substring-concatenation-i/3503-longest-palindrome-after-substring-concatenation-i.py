class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        # time: O(len(s) * len(t))
        # space: O(len(s) * len(t))
        # method: LCS DP
        t = t[::-1]
        n = len(s)
        m = len(t)
        lcs = [[0] * m for _ in range(n)]
        lcs_s = [0] * n
        lcs_t = [0] * m
        for i in range(n): # row -> s
            for j in range(m): # col -> t
                if s[i] == t[j]:    
                    if i == 0 or j == 0:
                        lcs[i][j] = 1
                    else:
                        lcs[i][j] = lcs[i - 1][j - 1] + 1
                lcs_s[i] = max(lcs_s[i], lcs[i][j])
                lcs_t[j] = max(lcs_t[j], lcs[i][j])
        
        def palindrome_length(index: int, text: str) -> tuple: # odd, even length # O(len(text))
            odd = 0
            left = right = index
            while left >= 0 and right < len(text) and text[left] == text[right]:
                odd += 1
                left -= 1
                right += 1
            odd = odd * 2 - 1
            
            even = 0
            left, right = index, index + 1
            while left >= 0 and right < len(text) and text[left] == text[right]:
                even += 1
                left -= 1
                right += 1
            even = even * 2
            return (odd, even)
        
        def longest_combined_palindrome(text: str, lcs: list) -> int:
            n = len(text)
            result = 0
            for i in range(n):
                odd, even = palindrome_length(i, text)
                length = max(odd, even)
                left = i - odd // 2 - 1
                if left >= 0:
                    length = max(length, odd + 2 * lcs[left])
                left = i - even // 2
                if left >= 0:
                    length = max(length, even + 2 * lcs[left])
                
                result = max(result, length)
            return result
        
        result = max(longest_combined_palindrome(s, lcs_s), longest_combined_palindrome(t, lcs_t))
        return result