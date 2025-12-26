class Solution:
    def bestClosingTime(self, customers: str) -> int:
        arr = [int(ch == 'Y') for ch in customers]
        n = len(arr)
        for i in range(1, n):
            arr[i] += arr[i - 1]
        
        def rangeSum(l: int, r: int) -> int:
            if l > r:
                return 0
            if l == 0:
                return arr[r]
            return arr[r] - arr[l - 1]
        
        penalty = n - rangeSum(0, n - 1)
        earliestHour = n
        for i in range(n - 1, -1, -1):
            # if we close at i'th hour
            # count N from [0 -> i - 1] from sub array
            # count Y from [i, n - 1] from sub array
            # i - rangeSum(0, i - 1)
            curPenalty = i - rangeSum(0, i - 1) + rangeSum(i, n - 1)
            # print(i, curPenalty)
            if penalty >= curPenalty:
                penalty = curPenalty
                earliestHour = i
        
        return earliestHour
