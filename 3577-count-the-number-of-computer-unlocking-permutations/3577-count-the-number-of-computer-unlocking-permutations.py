class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if min(complexity) != complexity[0] or Counter(complexity)[complexity[0]] != 1:
            return 0
        n = len(complexity)
        res = 1
        mod = int(1e9 + 7)
        for i in range(1, n):
            res = (res * i) % mod
        return res