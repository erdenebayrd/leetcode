class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        arr = [0] * n
        if s[n - 1] == "0":
            arr[n - 1] = 1
        for i in range(n - 2, -1, -1):
            arr[i] = arr[i + 1]
            if not (s[i] == "1" or (s[i] == "0" and s[i + 1] == s[i])):
                arr[i] += 1
        res = 0
        for i in range(n):
            if s[i] == '1':
                res += arr[i]
        return res