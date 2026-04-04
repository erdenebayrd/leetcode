class SegmentTree:
    def __init__(self, n: int) -> None:
        self.size = 0
        self.n = n
        self.st = [float('-inf')] * 4 * n

    def query(self, lastK: int) -> int: # max of lastK elements
        return self.__query(1, 0, self.n - 1, max(0, self.size - lastK), self.size - 1)

    def __query(self, pointer: int, left: int, right: int, queryLeft: int, queryRight: int) -> int:
        if left > right or left > queryRight or right < queryLeft:
            return float('-inf')
        if left >= queryLeft and right <= queryRight:
            return self.st[pointer]
        leftMax = self.__query(2 * pointer, left, (left + right) // 2, queryLeft, queryRight)
        rightMax = self.__query(2 * pointer + 1, (left + right) // 2 + 1, right, queryLeft, queryRight)
        return max(leftMax, rightMax)

    def __add(self, pointer: int, left: int, right: int, position: int, value: int) -> None: # O(log N)
        if left > right or left > position or right < position:
            return
        if left == position and right == position:
            self.st[pointer] = value
            return
        self.__add(2 * pointer, left, (left + right) // 2, position, value)
        self.__add(2 * pointer + 1, (left + right) // 2 + 1, right, position, value)
        self.st[pointer] = max(self.st[2 * pointer], self.st[2 * pointer + 1])

    def add(self, value: int) -> None: # O(log N)
        self.__add(1, 0, self.n - 1, self.size, value)
        self.size += 1

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # time: O(N Log N)
        # space: O(N)
        # method: DP + Segment Tree
        n = len(nums)
        # st = SegmentTree(n)
        sl = SortedList()
        dp = nums[:]
        # st.add(dp[0])
        sl.add(dp[0])
        for i in range(1, n):
            # dp[i] = max(dp[i], st.query(k) + nums[i])
            dp[i] = max(dp[i], sl[-1] + nums[i])
            # st.add(dp[i])
            sl.add(dp[i])
            if i >= k:
                sl.remove(dp[i - k])
        result = max(dp)
        # print(dp)
        return result