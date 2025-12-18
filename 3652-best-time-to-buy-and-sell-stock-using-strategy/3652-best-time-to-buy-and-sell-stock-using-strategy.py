class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        profit = [prices[i] * strategy[i] for i in range(n)]
        diff = [[-profit[i] for i in range(n)], [prices[i] - profit[i] for i in range(n)]]
        for i in range(1, n):
            diff[0][i] += diff[0][i - 1]
            diff[1][i] += diff[1][i - 1]

        def rangeSum(l: int, r: int, idx: int) -> int:
            if l == 0:
                return diff[idx][r]
            return diff[idx][r] - diff[idx][l - 1]
        
        curSum = sum(profit)
        res = curSum
        for stIdx in range(n - k + 1):
            cur = curSum
            cur += rangeSum(stIdx, stIdx + k // 2 - 1, 0)
            cur += rangeSum(stIdx + k // 2, stIdx + k - 1, 1)
            res = max(res, cur)
        return res