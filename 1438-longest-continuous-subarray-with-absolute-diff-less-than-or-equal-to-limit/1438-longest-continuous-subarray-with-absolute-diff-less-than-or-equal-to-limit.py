class SWAG:
    def __init__(self):
        self.window_max = float("-inf")
        self.window_min = float("inf")
        self.window = [] # single values
        self.suffix = [] # tuple for min/max values
    
    def append(self, value: int):
        self.window_max = max(self.window_max, value)
        self.window_min = min(self.window_min, value)
        self.window.append(value)

    def popleft(self):
        if not self.suffix:
            min_value = max_value = self.window[-1]
            while self.window:
                min_value = min(min_value, self.window[-1])
                max_value = max(max_value, self.window[-1])
                self.suffix.append((min_value, max_value))
                self.window.pop()
            self.window_max = float("-inf")
            self.window_min = float("inf")
        self.suffix.pop()

    def get_min(self) -> int:
        value = self.window_min
        if self.suffix:
            suffix_min_value, _ = self.suffix[-1]
            value = min(value, suffix_min_value)
        return value

    
    def get_max(self) -> int:
        value = self.window_max
        if self.suffix:
            _, suffix_max_value = self.suffix[-1]
            value = max(value, suffix_max_value)
        return value


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        if I can imagine that I can find an min and max element of every subarray from [left, right] by O(1)
        I can do a sliding window
        if left to right sub array is valid I need to extend it into right by one by one.
        when it reach the limit, we can reduce the window to left -> left + 1, and so on until sub array would become valid

        now the problem is to find min/max value of any given subarray

        option 1
            - using a monotonic queue
        
        option 2
            - SWAG sliding window aggregation
        """

        # # ------------------------- option 1 -------------------------
        # # time: O(N)
        # # space: O(N)
        # # method: sliding window + monotonic queue

        # min_queue = deque() # strictly increasing
        # max_queue = deque() # strictly decreasing
        # left = 0
        # n = len(nums)
        # result = 0
        # for right in range(n):
        #     while min_queue and nums[min_queue[-1]] > nums[right]:
        #         min_queue.pop()
        #     min_queue.append(right)

        #     while max_queue and nums[max_queue[-1]] < nums[right]:
        #         max_queue.pop()
        #     max_queue.append(right)

        #     while nums[max_queue[0]] - nums[min_queue[0]] > limit:
        #         if min_queue[0] <= left:
        #             min_queue.popleft()
        #         if max_queue[0] <= left:
        #             max_queue.popleft()
        #         left += 1
        #     result = max(right - left + 1, result)
        # return result

        # ------------------------- option 2 -------------------------
        # time: O(N)
        # space: O(N)
        # method: sliding window + swag
        n = len(nums)
        left = 0
        result = 0
        swag = SWAG()
        for right in range(n):
            swag.append(nums[right])
            while swag.get_max() - swag.get_min() > limit: # O(1)
                swag.popleft()
                left += 1
            result = max(result, right - left + 1)
        return result