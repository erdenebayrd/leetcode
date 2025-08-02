class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        dp = [0] * (n + 1)
        jobs = [(0, 0, 0)]
        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[1])
        for i in range(1, n + 1):
            st, ed, wage = jobs[i]
            lo, hi = 0, i
            while lo + 1 < hi:
                md = (lo + hi) // 2
                if jobs[md][1] <= st:
                    lo = md
                else:
                    hi = md
            dp[i] = max(dp[i - 1], dp[lo] + wage)
        return dp[n]