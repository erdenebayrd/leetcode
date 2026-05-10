class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        """
            what if target array is all [0, 0, 0, ... , 0]
            that case we can chose max absolute elements of subarray which is all values are >= 0 or all values are < 0

            similarly to this, we only can generate a new array, lets call is "diff" it contains what number needed to be added on nums[i] then become target[i]

            if there is tie on nums[i] == target[i], we can just set current diff is 0 after adding it into total cost

            then we can work on "diff" array and it's target is all 0s [0, 0, 0, 0, ... , 0]
            so actually we don't need to create new array since save the memory usage.
            we can only compute diff by each element one by one and reuse that variable again and again all the indices
        """
        # time: O(N)
        # space: O(1)
        # method: dividing int segments by down and up or (up and down on minus diff)
        n = len(nums)
        result = increment = decrement = 0
        for i in range(n):
            diff = target[i] - nums[i]
            if diff > 0:
                if increment < diff:
                    result += diff - increment
                increment = diff
                decrement = 0
            elif diff < 0:
                if diff < decrement:
                    result += decrement - diff
                decrement = diff
                increment = 0
            else:
                increment = decrement = 0
        return result