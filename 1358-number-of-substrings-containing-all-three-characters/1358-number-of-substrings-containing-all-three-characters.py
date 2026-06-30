class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # time: O(N)
        # space: O(1)
        # method: sliding window
        a = b = c = 0
        left = 0
        result = 0
        n = len(s)
        for right in range(n):
            if s[right] == "a":
                a += 1
            elif s[right] == "b":
                b += 1
            else:
                c += 1
            while a > 0 and b > 0 and c > 0:
                result += n - right
                if s[left] == 'a':
                    a -= 1
                elif s[left] == 'b':
                    b -= 1
                else:
                    c -= 1
                left += 1
        return result