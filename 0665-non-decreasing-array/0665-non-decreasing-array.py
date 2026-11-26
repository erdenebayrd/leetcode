class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # time: O(N)
        # space: O(1)
        # method: simulation

        def check(left: int, right: int) -> bool: # O(n)
            for i in range(left, right):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                # make nums[i + 1] = nums[i]
                if ((i + 2 == n) or (i + 2 < n and nums[i] <= nums[i + 2])) and check(i + 2, n - 1):
                    return True

                # make nums[i] = nums[i + 1]
                if ((i - 1 >= 0 and nums[i - 1] <= nums[i + 1]) or (i == 0)) and check(i + 1, n - 1):
                    return True

                return False
        return True