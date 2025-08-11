class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        p = 1
        m = 32 # bits
        powers = {}
        mod = int(1e9 + 7)
        for i in range(m * (m + 1) // 2): #
            powers[i] = p
            p = (p * 2) % mod
        arr = []
        for i in range(32, -1, -1):
            x = 1 << i
            if n >= x:
                n -= x
                arr.append(i)
        arr = arr[::-1]
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        res = []
        for l, r in queries:
            x = arr[r]
            if l > 0:
                x -= arr[l - 1]
            res.append(powers[x])
        return res