class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                arr[i][j] = math.gcd(nums[i], nums[j])

        # for i in range(n):
        #     print(arr[i])
        
        inf = int(1e6)

        @cache
        def solve(idx: int) -> int:
            if idx >= n:
                return 0
            res = inf
            for i in range(idx, n):
                if arr[idx][i] == 1:
                    continue
                res = min(res, 1 + solve(i + 1))
            return res

        res = solve(0)
        if res >= inf:
            res = -1
        return res