class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        index = 0
        result = [''] * n
        count = Counter(s)
        mid = ""
        for code in range(ord('a'), ord('z') + 1):
            ch = chr(code)
            while count[ch] >= 2:
                result[index] = result[n - 1 - index] = ch
                index += 1
                count[ch] -= 2
            if count[ch] == 1:
                assert mid == ""
                mid = ch
        if mid:
            result[n // 2] = mid
        return "".join(result)