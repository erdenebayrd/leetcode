class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        slFirstArr = SortedList(nums[:n])
        slSecondArr = SortedList(nums[n:])
        sumFirst = sum(slFirstArr[:n])
        sumSecond = sum(slSecondArr[-n:])
        # print(sumSecond)
        res = sumFirst - sumSecond
        
        # for i in range(n, 2 * n):
        #     x = nums[i]
        #     slSecondArr.remove(x)
        #     slFirstArr.add(x)
        #     sumFirst = sum(slFirstArr[:n])
        #     sumSecond = sum(slSecondArr[-n:])
        #     res = min(res, sumFirst - sumSecond)
        
        for i in range(n, 2 * n):
            x = nums[i]
            # x should be removed from slSecondArr and added into slFirstArr
            # assert x in slSecondArr
            idx = slSecondArr.bisect_left(x)
            sizeSlSecondArr = len(slSecondArr)
            slSecondArr.pop(idx)
            if idx >= sizeSlSecondArr - n: # idx was included last n elements of slSecondArr
                sumSecond -= x
                sumSecond += slSecondArr[-n]

            # x has to be added into slFirstArr
            slFirstArr.add(x)
            idx = slFirstArr.bisect_left(x)
            if idx < n:
                sumFirst -= slFirstArr[n]
                sumFirst += x
            res = min(res, sumFirst - sumSecond)
        return res