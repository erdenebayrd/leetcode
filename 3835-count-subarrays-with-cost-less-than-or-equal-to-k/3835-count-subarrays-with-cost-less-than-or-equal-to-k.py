from collections import deque

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # cost = (max(nums[l..r]) - min(nums[l..r])) * (r - l + 1).
        #        [1,3,2], k = 4
        # left.   ^    
        # right.  ^
        
        # step 1
        # cost = (1-1) * 1 = 0 <= 4 True
        # increase counter by 1, counter += 1,  counter = 1
        
        # step 2
        # cost = (3-1) * 2 = 4 <= 4 True
        # increase counter by 2, counter += 2,  counter = 3, end at right pointer, how many subarrays are valid. since left -> right is valid, we need to count all subarrays, [left, right], [left + 1, right] ..... [right, right]
        # counter += right - left + 1

        # step 3
        # cost = (3-2) * 2 =>.    2 <= 4 True
        # counter += right - left + 1 = 2 - 1 + 1 = 2,   counter = 5

        # handle finding max and min between each [left, right] in O(1), we can do it by monotonic stack + sliding window
        # how?
        # maxValue = [] this stack contains index of nums, maxValue be decreased
        # [2]

        # minValue = [] this stack contains index of nums, minValue be increased
        # [2]

        # time: O(N)
        # space: O(N) store monotonic stack which can be N length

        #        [1,3,2], k = 4
        # left.     ^    
        # right.      ^
        # minValue: [2]
        # maxValue: [1, 2]
        # counter = 0 + 1 + 2 + 2 = 5

        counter = 0
        left = 0
        n = len(nums)
        minValue = deque() # index of nums
        maxValue = deque() # index of nums
        for right in range(n):
            while minValue and nums[minValue[-1]] > nums[right]: # minValue be increased
                minValue.pop()
            minValue.append(right) # right is the index [0, 2]

            while maxValue and nums[maxValue[-1]] < nums[right]: # maxValue be decreased
                maxValue.pop() # [_]
            maxValue.append(right) # [1, 2] 2

            # else: # cost > k
            while left < right and (nums[maxValue[0]] - nums[minValue[0]]) * (right - left + 1) > k: # 6 > 4 True
                # when left goes right by 1, we need to check minValue and maxValue which might containing "left" index, if it is, we would remove left from the stacks
                if minValue[0] == left: # minValue: [2]
                    minValue.popleft()   
                if maxValue[0] == left: # maxValue: [1, 2]
                    maxValue.popleft()
                left += 1

            # cost = (max(nums[l..r]) - min(nums[l..r])) * (r - l + 1).
            cost = (nums[maxValue[0]] - nums[minValue[0]]) * (right - left + 1) # cost = (3 - 2) * (2) = 2, 2 <= 4 True
            if cost <= k: # 2 <= 4 TRUE
                counter += (right - left + 1) # counter += [1, 2] += 2 - 1 + 1 += 2

        return counter