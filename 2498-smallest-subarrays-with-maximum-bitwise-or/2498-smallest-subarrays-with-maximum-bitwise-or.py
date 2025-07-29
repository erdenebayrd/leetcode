class Solution:
    def toBinary32(self, x: int) -> List[int]:
        res = []
        for i in range(32):
            res.append((x >> i) & 1)
        return res[::-1]

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # time: O(N * Log M)  M = 32
        # space: O(N * Log M)
        # method: bit manupilate
        arr = []
        dp = []
        for x in nums:
            arr.append(self.toBinary32(x))
            dp.append([-1] * 32)
        n = len(nums)
        for i in range(32):
            dp[-1][i] = n - 1
        res = [1]
        for i in range(n - 2, -1, -1):
            cur = i
            for j in range(32):
                arr[i][j] += arr[i + 1][j]
                if arr[i][j] > arr[i + 1][j]:
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i + 1][j]
                if arr[i][j] == 0:
                    continue
                cur = max(cur, dp[i][j])
            res.append(cur - i + 1)
        return res[::-1]