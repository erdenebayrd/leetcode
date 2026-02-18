class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # # tc: O(N)
        # # sc: O(N)
        # n = len(nums)
        # existed = [False] * (n + 1)

        # for i in range(n):
        #     if 1 <= nums[i] <= n:
        #         existed[nums[i]] = True
        # for i in range(1, n + 1):
        #     if existed[i] is False:
        #         return i
        # return n + 1

        # time: O(N)
        # space: O(1)
        n = len(nums)
        for i in range(n):
            if 1 <= nums[i] <= n:
                continue
            nums[i] = float("inf")
        
        for i in range(n):
            if 1 <= nums[i] <= n:
                index = nums[i] - 1
                if nums[index] > 0:
                    nums[index] = -nums[index]
            elif -n <= nums[i] <= -1: # negative number
                index = -nums[i] - 1
                if nums[index] > 0:
                    nums[index] = -nums[index]

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1