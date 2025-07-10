class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        beg = 0
        arr = []
        for i in range(n):
            arr.append(startTime[i] - beg)
            beg = endTime[i]
        arr.append(eventTime - beg)
        # print(arr)
        res = 0
        sl = SortedList([arr[i] for i in range(1, len(arr))])
        for i in range(1, len(arr)):
            sl.remove(arr[i])
            b = endTime[i - 1] - startTime[i - 1]
            res = max(res, arr[i] + arr[i - 1])
            if sl and sl[-1] >= b:
                res = max(res, arr[i] + arr[i - 1] + b)
            sl.add(arr[i - 1])
        return res