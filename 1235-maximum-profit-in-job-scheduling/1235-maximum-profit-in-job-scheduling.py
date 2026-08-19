class Solution:
    def jobScheduling(self, start_time: List[int], end_time: List[int], profit: List[int]) -> int:
        # time: O(n log n)
        # space: O(n)
        # method: DP + binary search + prefix max
        n = len(profit)
        jobs = [(start_time[i], end_time[i], profit[i]) for i in range(n)]
        jobs.sort(key=lambda x: x[1])
        # print(jobs)
        dp = [0] * n
        prefix_max = [0] * n
        for i in range(n):
            left, _, wage = jobs[i]
            low, high = -1, i
            while low + 1 < high:
                mid = (low + high) // 2
                if jobs[mid][1] <= left:
                    low = mid
                else:
                    high = mid
            dp[i] = wage
            prefix_max[i] = max(prefix_max[i - 1], dp[i])
            if low == -1:
                continue
            dp[i] += prefix_max[low]
            prefix_max[i] = max(prefix_max[i - 1], dp[i])
        # print(dp)
        # print(prefix_max)
        return max(dp)