class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        arr = [0]
        beg = 0
        for i in range(n):
            arr.append(startTime[i] - beg)
            beg = endTime[i]
            arr[-1] += arr[-2]
        arr.append(eventTime - beg)
        arr[-1] += arr[-2]
        res = 0
        for i in range(k + 1, len(arr)):
            res = max(res, arr[i] - arr[i - k - 1])
        return res