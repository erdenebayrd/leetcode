import heapq

class SparseTable:
    def __init__(self, nums: list) -> None:
        self.n = len(nums)
        cols = int(log2(self.n)) + 1
        self.st_max = [[0] * cols for _ in range(self.n)]
        self.st_min = [[0] * cols for _ in range(self.n)]

        for i in range(self.n):
            self.st_max[i][0] = nums[i]
            self.st_min[i][0] = nums[i]

        for col in range(1, cols):
            for i in range(self.n):
                right = i + (1 << col) - 1
                if right < self.n:
                    self.st_max[i][col] = max(self.st_max[i][col - 1], self.st_max[right - (1 << (col - 1)) + 1][col - 1])
                    self.st_min[i][col] = min(self.st_min[i][col - 1], self.st_min[right - (1 << (col - 1)) + 1][col - 1])
    
    def get_min(self, left: int, right: int) -> int:
        if left > right:
            return 0
        length = right - left + 1
        level = int(log2(length))
        value = min(self.st_min[left][level], self.st_min[right - (1 << level) + 1][level])
        return value
    
    def get_max(self, left: int, right: int) -> int:
        if left > right:
            return 0
        length = right - left + 1
        level = int(log2(length))
        value = max(self.st_max[left][level], self.st_max[right - (1 << level) + 1][level])
        return value

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        """
        first observation is if we choose range [0, n - 1], that would be the max value among all subarrays
        then we need to choose second range which can be [0, n - 2] or [1, n - 1], we'll choose the max one.
        if [0, n - 2] is chosen, we need to append next elements which is [0, n - 3], [1, n - 2]
        we can just imagine there is a 2D array which is diff between max - min values in a range (row as left, col as right)
        start at last row which is max values (diffs of max and min) then move RIGHT pointer to left by one if the LEFT & RIGHT is chosen
        """
        # time: O((N + K) * log N)
        # space: O(N)
        # method: heap + sparse table/segment tree
        n = len(nums)
        max_heap = []
        st = SparseTable(nums)
        right = n - 1
        for left in range(n):
            max_value = st.get_max(left, right)
            min_value = st.get_min(left, right)
            value = max_value - min_value
            heapq.heappush(max_heap, (-value, left, right))
        
        result = 0
        for _ in range(k):
            value, left, right = heapq.heappop(max_heap)
            # print(-value, left, right)
            result -= value
            max_value = st.get_max(left, right - 1)
            min_value = st.get_min(left, right - 1)
            value = max_value - min_value
            heapq.heappush(max_heap, (-value, left, right - 1))
        return result
