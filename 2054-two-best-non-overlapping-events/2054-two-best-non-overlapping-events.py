from typing import List

class SegmentTree:
    def __init__(self, values: List[int]) -> None:
        self.values = values
        self.tree = [0] * 4 * len(values)
        self.__build(1, 0, len(values) - 1)
    
    def __build(self, pointer: int, left: int, right: int) -> None:
        if left == right:
            self.tree[pointer] = self.values[right]
            return
        self.__build(2 * pointer, left, (left + right) // 2)
        self.__build(2 * pointer + 1, (left + right) // 2 + 1, right)
        self.tree[pointer] = max(self.tree[2 * pointer], self.tree[2 * pointer + 1])

    def rangeMax(self, pointer: int, left: int, right: int, queryLeft: int, queryRight: int) -> int:
        if left > right or left > queryRight or right < queryLeft:
            return 0
        if queryLeft <= left and right <= queryRight:
            return self.tree[pointer]
        leftValue = self.rangeMax(2 * pointer, left, (left + right) // 2, queryLeft, queryRight)
        rightValue = self.rangeMax(2 * pointer + 1, (left + right) // 2 + 1, right, queryLeft, queryRight)
        return max(leftValue, rightValue)

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda event: event[1])
        print(events)
        values = [value for _, _, value in events]
        result = max(values) # if I chose only one event, max values would be the answer
        segmentTree = SegmentTree(values=values)
        for i in range(n):
            # find j'th index, under ==>> "j < i and events[j][1] <= events[i][0]"
            low, high = -1, i
            while low + 1 < high:
                middle = (low + high) // 2
                if events[middle][1] < events[i][0]:
                    low = middle
                else: # events[middle][1] > events[i][0]:
                    high = middle
            print(i, low)
            if low == -1: # means we didn't found any j under the condition
                continue
            value = segmentTree.rangeMax(1, 0, n - 1, 0, low)
            result = max(result, value + events[i][2])
        return result