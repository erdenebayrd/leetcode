class SegmentTree:
    def __init__(self, size: int) -> None:
        self.st = [0] * 4 * size
        self.size = size

    def get_max(self, left: int, right: int) -> int:
        return self.__get_max(1, 1, self.size, left, right)
    
    def __get_max(self, pointer: int, left: int, right: int, query_left: int, query_right: int) -> int:
        if left > right or left > query_right or right < query_left:
            return 0
        if left >= query_left and right <= query_right:
            return self.st[pointer]
        left_max = self.__get_max(2 * pointer, left, (left + right) // 2, query_left, query_right)
        right_max = self.__get_max(2 * pointer + 1, (left + right) // 2 + 1, right, query_left, query_right)
        current_max = max(left_max, right_max)
        return current_max

    def update(self, position: int, value: int) -> None:
        self.__update(1, 1, self.size, position, value)

    def __update(self, pointer: int, left: int, right: int, position: int, value: int) -> None:
        if left > right or left > position or right < position:
            return
        if left == position == right:
            self.st[pointer] = value
            return
        self.__update(2 * pointer, left, (left + right) // 2, position, value)
        self.__update(2 * pointer + 1, (left + right) // 2 + 1, right, position, value)
        self.st[pointer] = max(self.st[2 * pointer], self.st[2 * pointer + 1])

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        # time: O(N * log N) N is the max value of nums
        # space: O(N)
        # method: Segment Tree + DP
        size = max(nums)
        segment_tree = SegmentTree(size)
        for number in nums:
            left = max(1, number - k)
            right = number - 1
            prev = segment_tree.get_max(left, right)
            curr = segment_tree.get_max(number, number)
            if prev + 1 > curr:
                segment_tree.update(number, prev + 1)
        result = segment_tree.get_max(1, size)
        return result