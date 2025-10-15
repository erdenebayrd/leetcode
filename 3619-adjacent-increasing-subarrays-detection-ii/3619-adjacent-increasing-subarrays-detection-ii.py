class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(N)
        # method: sliding window
        arr = []
        n = len(nums)
        curStart = 0
        for curEnd in range(1, n):
            if nums[curEnd - 1] >= nums[curEnd]:
                arr.append(curEnd - curStart)
                curStart = curEnd
        arr.append(n - curStart)
        res = 0
        for curLength in arr:
            res = max(res, curLength // 2)
        for i in range(1, len(arr)):
            res = max(res, min(arr[i], arr[i - 1]))
        return res