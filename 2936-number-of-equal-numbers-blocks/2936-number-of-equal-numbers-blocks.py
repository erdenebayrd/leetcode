# Definition for BigArray.
# class BigArray:
#     def at(self, index: long) -> int:
#         pass
#     def size(self) -> long:
#         pass
class Solution(object):
    def countBlocks(self, nums: Optional['BigArray']) -> int:
        """
        I can use a binary search to find first and last occurrences of each values
        then count total distinct values in this big array

        total distinct values are N
        """
        # # time: O(N * log(len(nums)))
        # # space: O(1)
        # # method: binary search

        # length = nums.size()
        # if length <= 1:
        #     return length
        # result = 0
        # index = 0
        # while index < length:
        #     value = nums.at(index)
        #     low, high = index - 1, length
        #     while low + 1 < high:
        #         mid = (low + high) // 2
        #         if nums.at(mid) != value:
        #             high = mid
        #         else:
        #             low = mid
        #     result += 1
        #     index = low + 1
        # return result

        # time: O(N * Log (len(nums)) ^ 2)
        # space: O(log(nums))
        # method: binary indexed search
        
        def findNext(index: int, value: int) -> int:
            length = nums.size()
            if index >= length or nums.at(index) != value:
                return index
            distance = 1
            current = index
            while index + distance < length and nums.at(index + distance) == value:
                current = index + distance
                distance <<= 1
            return findNext(current + 1, value)

        result = 0
        index = 0
        length = nums.size()
        while index < length:
            value = nums.at(index)
            index = findNext(index, value)
            result += 1
        return result