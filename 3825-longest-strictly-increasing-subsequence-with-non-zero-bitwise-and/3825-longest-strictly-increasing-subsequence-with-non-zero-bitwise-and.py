import bisect

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        def longesIncreasingSubsequence(arr: List[int]) -> int:
            if len(arr) == 0:
                return 0
            subArray = [arr[0]]
            for i in range(1, len(arr)):
                if arr[i] > subArray[-1]:
                    subArray.append(arr[i])
                else:
                    idx = bisect.bisect_left(subArray, arr[i])
                    subArray[idx] = arr[i]
            return len(subArray)
        
        n = len(nums)
        res = 0
        for bit in range(30):
            cur = []
            for i in range(n):
                if (nums[i] >> bit) & 1:
                    cur.append(nums[i])
            res = max(res, longesIncreasingSubsequence(cur))
        return res