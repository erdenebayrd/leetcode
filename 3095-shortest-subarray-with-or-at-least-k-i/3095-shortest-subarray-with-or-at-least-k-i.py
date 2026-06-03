class SWAG:
    def __init__(self) -> None:
        self.in_stack = [] # contains tuple (first value is the number added, second value is current OR of all values in in_stack)
        self.out_stack = []

    def append(self, number: int) -> None:
        in_aggregation = number
        if self.in_stack:
            in_aggregation |= self.in_stack[-1][-1]
        self.in_stack.append((number, in_aggregation))
    
    def pop_left(self) -> None:
        if not self.out_stack: # if out_stack is empty
            out_aggregation = 0
            while self.in_stack:
                number, _ = self.in_stack.pop()
                out_aggregation |= number
                self.out_stack.append((number, out_aggregation))
        
        self.out_stack.pop()
    
    def query(self) -> int: # in this case, returns logical OR of the sliding window O(1)
        in_aggregation = 0
        if self.in_stack:
            in_aggregation |= self.in_stack[-1][-1]
        out_aggregation = 0
        if self.out_stack:
            out_aggregation |= self.out_stack[-1][-1]
        return in_aggregation | out_aggregation

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # time: O(N)
        # space: O(N)
        # method: Sliding Window Aggregation
        n = len(nums)
        left = 0
        swag = SWAG()
        result = float('inf')
        for right in range(n):
            swag.append(nums[right])
            while left <= right and swag.query() >= k:
                result = min(result, right - left + 1)
                swag.pop_left()
                left += 1
        if result == float("inf"):
            result = -1
        return result