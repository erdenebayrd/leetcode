import heapq
from typing import List
from sortedcontainers import SortedList

# class SegmentTree:
#     def __init__(self, size: int) -> None:
#         self.st = [0] * 4 * size

#     def update(self, p: int, l: int, r: int, pos: int, val: int) -> None:
#         if l > r or l > pos or r < pos:
#             return
#         if l == pos and r == pos:
#             self.st[p] = val
#             return
#         self.update(2 * p, l, (l + r) // 2, pos, val)
#         self.update(2 * p + 1, (l + r) // 2 + 1, r, pos, val)
#         self.st[p] = self.st[2 * p] + self.st[2 * p + 1]
    
#     def getIndexOfFirstKElements(self, p: int, l: int, r: int, k: int) -> int:
#         if l == r: # leaf node
#             return r
#         if self.st[2 * p] >= k:
#             return self.getIndexOfFirstKElements(2 * p, l, (l + r) // 2, k) # go to left child
#         return self.getIndexOfFirstKElements(2 * p + 1, (l + r) // 2 + 1, r, k - self.st[2 * p]) # go to right one
    
#     def rangeSum(self, p: int, l: int, r: int, L: int, R: int) -> int:
#         if l > r or r < L or l > R:
#             return 0
#         if l >= L and r <= R:
#             return self.st[p]
#         return self.rangeSum(2 * p, l, (l + r) // 2, L, R) + self.rangeSum(2 * p + 1, (l + r) // 2 + 1, r, L, R)

#     # debug purpose only
#     def print(self, p: int, l: int, r: int) -> None:
#         if l > r:
#             return
#         if l == r:
#             print(self.st[p], end=" ")
#             return
#         self.print(2 * p, l, (l + r) // 2)
#         self.print(2 * p + 1, (l + r) // 2 + 1, r)
#         if p == 1: # root
#             print("")

class Solution:
    # def getIndexValueForSegmentTree(self, index: int) -> List[int, int]:
    #     value = self.nums[index]
    #     updatedIndex = self.positions[value][index]
    #     return updatedIndex, value

    # def addToSegmentTree(self, index: int) -> None:
    #     index, value = self.getIndexValueForSegmentTree(index)
    #     self.count.update(1, 0, self.n - 1, index, 1)
    #     self.values.update(1, 0, self.n - 1, index, value)
    
    # def removeFromSegmentTree(self, index: int) -> None:
    #     index, value = self.getIndexValueForSegmentTree(index)
    #     self.count.update(1, 0, self.n - 1, index, 0)
    #     self.values.update(1, 0, self.n - 1, index, 0)

    # def slidingWindow(self, left: int, right: int) -> None: # O(N * Log N) in total
    #     # adding
    #     while self.right < self.n and self.right < right:
    #         self.right += 1
    #         self.addToSegmentTree(self.right)
        
    #     # removing
    #     while self.left < self.n and self.left < left:
    #         self.removeFromSegmentTree(self.left)
    #         self.left += 1

    # def init(self, n: int, k: int, nums: List[int]) -> None:
    #     self.k = k - 1
    #     self.n = len(nums)
    #     self.nums = nums
    #     self.count = SegmentTree(self.n)
    #     self.values = SegmentTree(self.n)
    #     self.sortedList = sorted([(nums[i], i) for i in range(self.n)])
    #     self.positions = {}
    #     for i in range(len(self.sortedList)):
    #         value, index = self.sortedList[i]
    #         if value not in self.positions:
    #             self.positions[value] = {}
    #         self.positions[value][index] = i
    #     self.left, self.right = 0, -1 # range of current pool

    # def getSumOfLowestKElements(self, k: int) -> int: # O (Log N)
    #     # self.count.print(1, 0, self.n - 1)
    #     # self.values.print(1, 0, self.n - 1)
    #     rightIndex = self.count.getIndexOfFirstKElements(1, 0, self.n - 1, k) # O(Log N)
    #     sumOfValues = self.values.rangeSum(1, 0, self.n - 1, 0, rightIndex) # O(Log N)
    #     # print("""[{left}:{right}] = {sum}""".format(left=0, right=rightIndex, sum=sumOfValues))
    #     # print("-" * 100)
    #     return sumOfValues

    # def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
    #     # self.init(len(nums), k, nums) # O(N * Log N)
    #     # res = float('inf')

    #     # # time: O(N * Log N)
    #     # for i in range(1, self.n - self.k + 1): # i is the first index of second subArray
    #     #     rightMostIndex = min(i + dist, self.n - 1)
    #     #     self.slidingWindow(i + 1, rightMostIndex)
    #     #     # print(i, i + 1, rightMostIndex, self.count.st[1])
    #     #     # self.count.print(1, 0, self.n - 1)
    #     #     res = min(res, nums[0] + nums[i] + self.getSumOfLowestKElements(self.k - 1))
    #     # return res
    #     n = len(nums)
    #     sortedList = SortedList()
    #     for i in range(2, min(n, 2 + dist)):
    #         sortedList.add(nums[i])
    #     currentSum = sum(sortedList[:k-2])
    #     res = nums[0] + nums[1] + currentSum
    #     for i in range(2, n - k + 2): # i is the beginning of second subArray
    #         # remove i 'th element from sortedList and change currentSum if affected
    #         value = nums[i]
    #         index = sortedList.bisect_left(value)
    #         sortedList.pop(index) # O(Log N)
    #         if index < k - 2: # which means the value is in currentSum
    #             currentSum -= value
    #             if k - 3 < len(sortedList):
    #                 currentSum += sortedList[k - 3]
            
    #         # add i + dist 'th element into sortedList and change currentSum if it's affected
    #         if i + dist < n:
    #             value = nums[i + dist]
    #             sortedList.add(value)
    #             index = sortedList.bisect_left(value)
    #             if index < k - 2: # which means the value has to be added into currentSum
    #                 currentSum += value
    #                 if k - 2 < len(sortedList):
    #                     currentSum -= sortedList[k - 2]
    #         res = min(res, nums[0] + nums[i] + currentSum)
    #     return res
    
    # me at 2 years ago, it was actually very clever solution on c++, here I got the idea from my 2 years old code.
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        leftSortedList = SortedList() # which contains minimum/first k - 1 elements of range [i, i + dist]
        rightSortedList = SortedList() # which contains other elements of range [i, i + dist]
        currentSum = 0
        for i in range(1, dist + 2):
            value = nums[i]
            if len(leftSortedList) < k - 1:
                leftSortedList.add(value)
                currentSum += value
            else:
                if leftSortedList[-1] > value: # value need to be added into leftSortedList and last/max value of leftSortedList is need to be transitioned into rightSortedList
                    currentSum += value
                    leftSortedList.add(value)
                    currentSum -= leftSortedList[-1]
                    rightSortedList.add(leftSortedList[-1])
                    leftSortedList.pop()
                else:
                    rightSortedList.add(value)
        res = nums[0] + currentSum
        for i in range(2, n - dist):
            # add i + dist 'th value into left or right SortedList, before removing i - 1 'th element from left or right SortedList as adding value would be safe at first instead of removing element at first
            value = nums[i + dist]
            if leftSortedList[-1] > value: # value is needed to be added leftSortedList
                currentSum += value
                leftSortedList.add(value)
                currentSum -= leftSortedList[-1]
                rightSortedList.add(leftSortedList[-1])
                leftSortedList.pop()
            else:
                rightSortedList.add(value)
            
            # remove i - 1 'th element from left or right SortedList
            value = nums[i - 1]
            if value <= leftSortedList[-1]: # which means leftSortedList contains value in somewhere in a middle
                currentSum -= value
                leftSortedList.remove(value)
                currentSum += rightSortedList[0]
                leftSortedList.add(rightSortedList[0])
                rightSortedList.pop(0)
            else:
                rightSortedList.remove(value)
            
            res = min(res, nums[0] + currentSum)
        return res