from typing import List

class SegmentTree:
    def __init__(self, arr: List[int]) -> None: 
        self.n = len(arr)
        self.tree = [0] * 4 * self.n
        self.arr = arr
        self.build(1, 0, self.n - 1)
    
    def build(self, pointer: int, left: int, right: int) -> None: # O(N) visiting 2N - 1 nodes ( N leaf nodes, N - 1 non-leaf nodes)
        if left == right:
            self.tree[pointer] = right # index
            return
        self.build(2 * pointer, left, (left + right) // 2) # left sub tree
        self.build(2 * pointer + 1, (left + right) // 2 + 1, right) # right sub tree
        indexLeft = self.tree[2 * pointer]
        indexRight = self.tree[2 * pointer + 1]
        if self.arr[indexLeft] < self.arr[indexRight]:
            self.tree[pointer] = indexLeft
        else:
            self.tree[pointer] = indexRight
    
    def getMinimum(self, pointer: int, left: int, right: int, queryLeft: int, queryRight: int) -> int: # O(log N)
        if left > right or left > queryRight or right < queryLeft: # out of query range
            return -1
        if left >= queryLeft and right <= queryRight:
            return self.tree[pointer]
        indexLeft = self.getMinimum(2 * pointer, left, (left + right) // 2, queryLeft, queryRight) # left sub tree
        indexRight = self.getMinimum(2 * pointer + 1, (left + right) // 2 + 1, right, queryLeft, queryRight) # right sub tree
        if indexLeft == -1:
            return indexRight
        if indexRight == -1:
            return indexLeft
        if self.arr[indexLeft] < self.arr[indexRight]:
            return indexLeft
        return indexRight

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        area of [i, j] -> (j - i + 1) * min(heights[i..j])
        
        1. area of [0, n - 1] -> n * min(heights[0..n- 1])
        2. there is no other area in [0...n - 1] range, the only one is [1]
        3. we can divide the range [0...n-1] to 2 different range, 
            lets assume "i" is the index of minimum element from [0, n - 1]
            so, we can divide [0, i - 1], [i + 1, n - 1] then find those area
        4. the largest area will be max of all those areas
        
        Example
        index:   0, 1, 2, 3, 4, 5
        value:  [2, 1, 5, 6, 2, 3]
        min         ^             
        meaning ANY area of rectangle including "index" 1 won't be greather than 1 * 6, 1 is min height, 6 is the widest range (number of histogram heights)
        so that, I can divide problems into 2 different parts
            1. [0, 0]
            2. [2, 5]
        same calculation will happen

        - finding a min element index would be O(log N) time complexity using Segment Tree
        - dividing the heights array into parts would be total N parts
        time: O(N * log N)
        space: O(N)
        """
        # # time: O(N log N)
        # # space: O(N)
        # # method: Divide and Conquer + RMQ
        # segmentTree = SegmentTree(heights)
        # n = len(heights)

        # def area(left: int, right: int) -> int:
        #     if left > right:
        #         return 0
        #     index = segmentTree.getMinimum(1, 0, n - 1, left, right)
        #     currentArea = (right - left + 1) * heights[index]
        #     leftArea = area(left, index - 1)
        #     rightArea = area(index + 1, right)
        #     return max(currentArea, leftArea, rightArea)
        
        # return area(0, n - 1)

        # time: O(N)
        # space: O(N)
        # method: monotonic stack (prev/next smaller)
        n = len(heights)
        prev, next = [-1] * n, [n] * n # prev and next strictly smaller element indices
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                prev[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                next[i] = stack[-1]
            stack.append(i)

        area = 0
        for i in range(n):
            left = prev[i] + 1
            right = next[i] - 1
            width = right - left + 1
            area = max(area, width * heights[i])
        return area