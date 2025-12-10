class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 1_000_000_007
        dp = [0] * (n + 1)
        dp[0] = 1
        prefixDpSum = [0] * (n + 1)
        prefixDpSum[0] = dp[0]

        def getRangeSum(l: int, r: int) -> int:
            if l == 0:
                return prefixDpSum[r]
            return (prefixDpSum[r] - prefixDpSum[l - 1] + mod) % mod

        dqMin = deque() # first idx is the MIN
        dqMax = deque() # fist idx is the MAX

        j = 0
        def addDeque(idx: int) -> None:
            nonlocal j
            assert idx >= 0 and idx < n
            while dqMax and nums[dqMax[-1]] < nums[idx]:
                dqMax.pop()
            dqMax.append(idx)
            while dqMin and nums[dqMin[-1]] > nums[idx]:
                dqMin.pop()
            dqMin.append(idx)

            while nums[dqMax[0]] - nums[dqMin[0]] > k:
                j = min(dqMax[0], dqMin[0]) + 1
                if dqMax and dqMax[0] < dqMin[0]:
                    dqMax.popleft()
                elif dqMin and dqMin[0] < dqMax[0]:
                    dqMin.popleft()
        
        for i in range(n):
            addDeque(i)
            assert len(dqMax) > 0 and len(dqMin) > 0
            # farthestLeftIdx = min(dqMax[0], dqMin[0])
            dp[i + 1] = getRangeSum(j, i)
            prefixDpSum[i + 1] = (prefixDpSum[i] + dp[i + 1]) % mod
        
        # print(dqMax)
        # print(dqMin)
        # print("-" * 10)
        # print(dp)
        # print(prefixDpSum)
        return dp[n]