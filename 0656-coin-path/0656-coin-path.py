class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        inf = int(1e18)
        n = len(coins)
        coins = [inf if x == -1 else x for x in coins]
        
        @cache
        def solve(idx: int) -> int:
            if idx == n - 1:
                return coins[n - 1]
            res = inf
            for i in range(idx + 1, min(n, idx + maxJump + 1)):
                res = min(res, coins[idx] + solve(i))
            return res
        cost = solve(0)
        # print(cost)
        if cost >= inf:
            return []
        
        res = []
        def forwardTrack(idx: int):
            res.append(idx + 1)
            for i in range(idx + 1, min(idx + 1 + maxJump, n)):
                # print(i)
                if coins[idx] + solve(i) == solve(idx):
                    forwardTrack(i)
                    break

        forwardTrack(0)
        return res