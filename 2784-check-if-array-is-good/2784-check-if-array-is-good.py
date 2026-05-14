from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        """
        first observation is 
        * frequency of maximum number has to be exactly 2
        * all other numbers must be in [1 -> max_number - 1]
        * total length of an given array must be max_number + 1
        * frequency of all number must be 1 except the max_number
        """
        # time: O(N)
        # space: O(N)
        # method: counting
        count = Counter(nums)
        max_number = max(nums)
        if count[max_number] != 2:
            return False
        if len(nums) != max_number + 1:
            return False
        for number in nums:
            if not 1 <= number <= max_number:
                return False
            if number != max_number and count[number] != 1:
                return False
        return True