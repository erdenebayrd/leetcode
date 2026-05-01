class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # # time: O(N)
        # # space: O(N)
        # # method: prefix sum + greedy
        # """
        # step 1                            
        #                                   0.   1.  2.        n - 2.  n -1
        #                                   *.   *.  *            *      *
        # a0, a1, a2, ... , a(n-2), a(n-1), a0, a1, a2, ... , a(n-2), a(n-1)
        #                                    ^

        # step 2
        #                              0.   1.  2.      n - 2.  n -1
        #                              *.   *.  *          *     *
        # a0, a1, a2, ... , a(n-2), a(n-1), a0, a1, a2, ... , a(n-2), a(n-1)
        # """
        # n = len(nums)
        # result = 0
        # for i in range(n):
        #     result += i * nums[i]
        
        # nums = nums + nums
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i - 1]
        
        # def getRangeSum(left: int, right: int) -> int:
        #     if left == 0:
        #         return nums[right]
        #     return nums[right] - nums[left - 1]
        
        # current = result
        # for i in range(len(nums) - 1, n - 1, -1):
        #     current -= getRangeSum(i, i) * (n - 1)
        #     current += getRangeSum(i - n + 1, i - 1)
        #     result = max(result, current)
        # return result

        # -------------------------------- SPACE O(1) --------------------------------
        # time: O(N)
        # space: O(1)
        # method: math
        total = sum(nums)
        n = len(nums)
        result = 0
        for i in range(n):
            result += i * nums[i]
        current = result
        for i in range(n - 1, 0, -1):
            current += total - nums[i] * n
            result = max(result, current)
        return result