class SWAG:
    def __init__(self) -> None:
        self.in_stack = []
        self.out_stack = []
    
    def append(self, number: int) -> None:
        in_aggregation = number
        if self.in_stack:
            in_aggregation |= self.in_stack[-1][1]
        self.in_stack.append((number, in_aggregation))
    
    def pop_left(self) -> None:
        if not self.out_stack:
            out_aggregation = 0
            while self.in_stack:
                number, _ = self.in_stack.pop()
                out_aggregation |= number
                self.out_stack.append(out_aggregation)
        self.out_stack.pop()
    
    def query(self) -> int: # return current window's OR
        in_aggregation = 0
        if self.in_stack:
            in_aggregation |= self.in_stack[-1][1]
        out_aggregation = 0
        if self.out_stack:
            out_aggregation |= self.out_stack[-1]
        return in_aggregation | out_aggregation

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # time: O(N)
        # space: O(N)
        # method: Sliding window aggregation
        result = float("inf")
        left = 0
        n = len(nums)
        swag = SWAG()
        for right in range(n):
            swag.append(nums[right])
            result = min(result, abs(swag.query() - k))
            while left < right and swag.query() >= k:
                swag.pop_left()
                result = min(result, abs(swag.query() - k))
                left += 1
        return result