class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # time: O(N log N)
        # space O(N)
        # method: monotonic strictly increasing stack + binary search
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        if prefix[0] >= k:
            return 1
        
        result = float('inf')
        for i in range(1, n):
            prefix[i] += prefix[i - 1] + nums[i]
            if prefix[i] >= k:
                result = min(result, i + 1)
        
        stack = [] # contains index only
        for i in range(n):
            while stack and prefix[stack[-1]] >= prefix[i]:
                stack.pop()
            if stack:
                low, high = -1, len(stack)
                while low + 1 < high:
                    mid = (low + high) // 2
                    if prefix[i] - prefix[stack[mid]] >= k:
                        low = mid
                    else:
                        high = mid
                if low != -1:
                    result = min(result, i - stack[low])
            stack.append(i)
        if result == float("inf"):
            result = -1
        return result