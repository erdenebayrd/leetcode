class Solution:
    def splitArray(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(N)
        # method: prefix sum
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        
        is_increasing = [False] * n
        is_increasing[0] = True
        for i in range(1, n):
            is_increasing[i] = (nums[i - 1] < nums[i]) and is_increasing[i - 1]

        is_decreasing = [False] * n
        is_decreasing[n - 1] = True
        for i in range(n - 2, -1, -1):
            is_decreasing[i] = (nums[i] > nums[i + 1]) and is_decreasing[i + 1]
        
        def get_range_sum(left: int, right: int) -> int:
            if left == 0:
                return prefix[right]
            return prefix[right] - prefix[left - 1]
        
        result = float('inf')
        for i in range(n - 1):
            if is_increasing[i] and is_decreasing[i + 1]:
                left_sum = get_range_sum(0, i)
                right_sum = get_range_sum(i + 1, n - 1)
                diff = abs(left_sum - right_sum)
                result = min(result, diff)
        if result == float('inf'):
            result = -1
        return result