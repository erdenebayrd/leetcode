class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                c = int(sqrt(i * i + j * j))
                if c <= n and c * c == i * i + j * j:
                    res += 1
                    print(i, j, c)
                
        return res
