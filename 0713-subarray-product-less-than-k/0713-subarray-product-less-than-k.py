class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def mostRight(curIdx: int, curVal: int) -> tuple:
            if curVal >= k:
                return (-1, -1)
            for i in range(curIdx + 1, n):
                curVal *= nums[i]
                if curVal >= k:
                    return (i - 1, curVal // nums[i])
            return (n - 1, curVal)
        
        idx, val = mostRight(0, nums[0])
        res = idx + 1
        for i in range(1, n):
            if i > idx:
                val = nums[i]
                idx = i
            else:
                val = val // nums[i - 1]
            idx, val = mostRight(idx, val)
            print(idx)
            if idx == -1:
                continue
            res += idx - i + 1
        return res
        