class SegmentTree:
    def __init__(self, size: int) -> None:
        self.n = size
        self.st = [0] * size * 4
    
    def update(self, index: int, value: int) -> None:
        self.__update(1, 0, self.n - 1, index, value)
    
    def __update(self, pointer: int, left: int, right: int, position: int, value: int) -> None:
        if left > right or left > position or right < position:
            return
        if left == right == position:
            self.st[pointer] = value
            return
        self.__update(2 * pointer, left, (left + right) // 2, position, value)
        self.__update(2 * pointer + 1, (left + right) // 2 + 1, right, position, value)
        self.st[pointer] = max(self.st[2 * pointer], self.st[2 * pointer + 1])

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # time: O(N log N)
        # space: O(N)
        # method: Segment Tree
        intervals.sort(key=lambda x: (x[0], -x[1])) # sorting intervals by "left" value
        n = len(intervals)
        st = SegmentTree(n)
        count = n
        for i in range(n):
            _, right = intervals[i]
            if right <= st.st[1]:
                count -= 1
                continue
            st.update(i, right)
        return count