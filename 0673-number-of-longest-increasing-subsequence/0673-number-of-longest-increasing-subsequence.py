class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
            * first thing is to find the longest strictly increasing subsequence
            * count how many different strictly increasing longest subsequence
        
        for example

        * first part (finding longest length)
           1, 3, 5, 4, 7
        dp 1. 2. 3. 3. 4   -> the length of longest strictly increasing subsequence
                       R
              if value[L] < value[R]
                    dp[R] = max(dp[R], dp[L] + 1)
        maximum value of DP would become the length of longest strictly inc subseq

        * second part (counting how many longest strictly subseqs)
            one more dp for counting, lets call it "count_dp"
            - base: initially all indices of dp[i] which is equal to 1, count_dp[i] = 1
            - each index i, go through j where j < i and nums[j] < nums[i] and dp[j] + 1 == dp[i]
                count_dp[i] += count_dp[j]
            - lastly, sum up all count_dp[i] where dp[i] == length, that's the result
        """
        # time: O(N ^ 2) N is the length of given array
        # space: O(N)
        # method: DP
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        count_dp = [0] * n
        for i in range(n):
            if dp[i] == 1:
                count_dp[i] = 1
        
        for i in range(n):
            for j in range(i): # j < i
                if nums[j] < nums[i] and dp[j] + 1 == dp[i]:
                    count_dp[i] += count_dp[j]
        result = 0
        length = max(dp)
        for i in range(n):
            if dp[i] == length:
                result += count_dp[i]
        return result