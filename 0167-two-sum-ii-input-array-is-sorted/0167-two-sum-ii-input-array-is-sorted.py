class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # time: O(N)
        # space: O(1)
        # method: 2 pointers
        """
            since the given array is already sorted we can use 2 pointers without using any extra memory
            left pointer starts a first element
            right pointer starts at last element

                    [2, 7, 11, 15], target = 9
            left.    ^
            right               ^
            
            if current sum of left and right elmeents is greater than target
            every pair with right would be always greather than target
            all left pointers at [left, left + 1, left + 2 .... right - 1], with "right" pionter value alwasy be greater than target, since numbers array sorted

            similarly
            current sum of left and right elmeents is lower than target
            every right pointers left, and right => [left + 1, .... right - 3, right - 2, right - 1, right] always be lower than target since sorted array is given

            when left < right we do same thing until we find the pair whose sum is exactly equal to given target
            
        """
        n = len(numbers)
        left, right = 0, n - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                break
        return [left + 1, right + 1]