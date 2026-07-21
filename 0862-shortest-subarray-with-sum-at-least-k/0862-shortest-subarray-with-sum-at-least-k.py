from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        since the array can contains negative numbers, we can't do sliding window

        instead we can create a prefix sum array 
        p0, p1, p2, .....pi.. , pn - 1    
                          ^
        pi - pj >= k      closest j before i
        pj <= pi - k
        so, we need to create a monotonic strictly increasing array by prefix array

        ^
        |
        |                                            [*]
        |                                            /
        |           [*] ------       V              /
        |          /         ------ [*] ----       /
        |         /                         ---- [*] 
        |        /                     
        |      [*]                
        |      /
        |    [*]
        |
        |
        |
        -------------------------------------------->
        """
        # # time: O(N log N)
        # # space: O(N)
        # # method: monotinic stack + binary search
        # n = len(nums)
        # prefix = [0] * n
        # prefix[0] = nums[0]
        # for i in range(1, n):
        #     prefix[i] = nums[i] + prefix[i - 1]
        # result = float('inf')
        # stack = [] # indices of prefix array
        # for i in range(n):
        #     if prefix[i] >= k:
        #         result = min(result, i + 1)
        #     low, high = -1, len(stack)
        #     while low + 1 < high:
        #         mid = (low + high) // 2
        #         if prefix[i] - prefix[stack[mid]] >= k:
        #             low = mid
        #         else:
        #             high = mid
        #     if low != -1:
        #         result = min(result, i - stack[low])

        #     while stack and prefix[stack[-1]] >= prefix[i]:
        #         stack.pop()
        #     stack.append(i)
        # if result == float('inf'):
        #     result = -1
        # return result

        """
            improvement is if there is some j index found before i, that j index never will be used again after i since we are handling strictly increasing monotonic stack/queue
        """
        # time: O(N)
        # space: O(N)
        # method: monotonic increasing queue
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i - 1]
        queue = deque() # indices of prefix array
        result = float('inf')
        for i in range(n):
            if prefix[i] >= k:
                result = min(result, i + 1)
            while queue and prefix[i] - prefix[queue[0]] >= k:
                result = min(result, i - queue[0])
                queue.popleft()
            
            while queue and prefix[queue[-1]] >= prefix[i]:
                queue.pop()
            queue.append(i)
        if result == float('inf'):
            result = -1
        return result