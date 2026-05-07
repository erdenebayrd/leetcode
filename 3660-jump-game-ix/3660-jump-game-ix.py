class SegmentTree:
    def __init__(self, arr: List[int]) -> None:
        n = len(arr)
        self.stMin = [0] * 4 * n
        self.stMax = [0] * 4 * n
        self.arr = arr
        self.build(1, 0, n - 1)
    
    def build(self, pointer: int, left: int, right: int) -> None:
        if left == right:
            self.stMin[pointer] = left
            self.stMax[pointer] = right
            return
        self.build(2 * pointer, left, (left + right) // 2) # left child
        self.build(2 * pointer + 1, (left + right) // 2 + 1, right) # right child
        if self.arr[self.stMax[2 * pointer]] < self.arr[self.stMax[2 * pointer + 1]]:
            self.stMax[pointer] = self.stMax[2 * pointer + 1]
        else:
            self.stMax[pointer] = self.stMax[2 * pointer]
        if self.arr[self.stMin[2 * pointer]] < self.arr[self.stMin[2 * pointer + 1]]:
            self.stMin[pointer] = self.stMin[2 * pointer]
        else:
            self.stMin[pointer] = self.stMin[2 * pointer + 1]
    
    def queryMax(self, pointer: int, left: int, right: int, queryLeft: int, queryRight: int) -> int:
        if left > right or left > queryRight or right < queryLeft:
            return -1
        if left >= queryLeft and right <= queryRight:
            return self.stMax[pointer]
        leftIndex = self.queryMax(2 * pointer, left, (left + right) // 2, queryLeft, queryRight)
        rightIndex = self.queryMax(2 * pointer + 1, (left + right) // 2 + 1, right, queryLeft, queryRight)
        if leftIndex == -1 or rightIndex == -1:
            return max(leftIndex, rightIndex)
        if self.arr[leftIndex] < self.arr[rightIndex]:
            return rightIndex
        return leftIndex

    def queryMin(self, pointer: int, left: int, right: int, queryLeft: int, queryRight: int) -> int:
        if left > right or left > queryRight or right < queryLeft:
            return -1
        if left >= queryLeft and right <= queryRight:
            return self.stMin[pointer]
        leftIndex = self.queryMin(2 * pointer, left, (left + right) // 2, queryLeft, queryRight)
        rightIndex = self.queryMin(2 * pointer + 1, (left + right) // 2 + 1, right, queryLeft, queryRight)
        if leftIndex == -1 or rightIndex == -1:
            return max(leftIndex, rightIndex)
        if self.arr[leftIndex] < self.arr[rightIndex]:
            return leftIndex
        return rightIndex

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        # time: O(N log N)
        # space: O(N)
        # method: rmq + binary search
        n = len(nums)
        st = SegmentTree(nums)
        prefixMax = [0] * n
        prefixMax[0] = nums[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], nums[i])
        result = nums[:]

        def findLeftMostIndex(left: int, minIndex: int) -> int:
            low, high = left - 1, minIndex
            while low + 1 < high:
                mid = (low + high) // 2
                if prefixMax[mid] > nums[minIndex]:
                    high = mid
                else:
                    low = mid
            return high

        def repeat(left: int, right: int, maxIndex: int):
            minIndex = st.queryMin(1, 0, n - 1, maxIndex, right)
            leftIndex = findLeftMostIndex(left, minIndex)
            while True:
                minIndex2 = st.queryMin(1, 0, n - 1, leftIndex, right)
                if minIndex == minIndex2:
                    break
                minIndex = minIndex2
                leftIndex = findLeftMostIndex(left, minIndex)
            return leftIndex

        def solve(left: int, right: int) -> None:
            if left > right:
                return
            maxIndex = st.queryMax(1, 0, n - 1, left, right)
            leftIndex = repeat(left, right, maxIndex)
            # print(left, right, maxIndex, leftIndex)
            for i in range(leftIndex, right + 1):
                result[i] = nums[maxIndex]
            solve(left, leftIndex - 1)
        
        solve(0, n - 1)
        return result