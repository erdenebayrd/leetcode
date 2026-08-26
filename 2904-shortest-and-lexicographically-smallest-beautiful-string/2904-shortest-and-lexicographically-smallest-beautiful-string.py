class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # time: O(N ^ 2)
        # space: O(1) without considering the answer
        # method: sliding window + brute force
        n = len(s)
        result = ""
        length = n + 1
        ones = 0
        left = 0
        for right in range(n):
            ones += int(s[right])
            while ones == k:
                length = min(length, right - left + 1)
                ones -= int(s[left])
                left += 1

        for right in range(length - 1, n):
            left = right - length + 1
            substr = s[left:right + 1]
            ones = 0
            for ch in substr:
                ones += int(ch)

            if ones == k:
                if result == "":
                    result = substr
                else:
                    result = min(result, substr)
        
        return result