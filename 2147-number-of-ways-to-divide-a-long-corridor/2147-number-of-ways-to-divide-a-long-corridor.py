class Solution:
    def numberOfWays(self, corridor: str) -> int:
        cnt = Counter(corridor)
        if cnt["S"] == 2:
            return 1
        if cnt["S"] & 1 or cnt["S"] == 0:
            return 0
        arr = []
        cur = 0
        z = 0
        mod = 1_000_000_007
        for x in corridor:
            if x == "S":
                cur += 1
            if cur == 2:
                cur = 0
                arr.append(z + 1)
                z = 0
            if cur == 0 and x == "P":
                z += 1
        # print(arr)
        res = 1
        for i in range(1, len(arr)):
            res = (res * arr[i]) % mod
        return res