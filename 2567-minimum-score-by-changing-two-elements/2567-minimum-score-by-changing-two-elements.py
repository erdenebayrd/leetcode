import heapq

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # # # time: O(N log N)
        # # # space: O(N) for timsort
        # # # method: sorting + greedy

        # # nums.sort()

        # # # case 1 - first 2 nums
        # # result = nums[-1] - nums[2]

        # # # case 2 - last 2 nums
        # # result = min(nums[-3] - nums[0], result)

        # # # case 3 - first and last number in nums
        # # result = min(result, nums[-2] - nums[1])
        # # return result


        # # time: O(n)
        # # space: O(1)
        # # method: finding first 3 min nums, last 3 max nums
        # inf = float('inf')

        # mins = [inf, inf, inf]
        # maxs = [-inf, -inf, -inf]

        # for number in nums:
        #     index = 3
        #     for i in range(2, -1, -1):
        #         if number >= mins[i]:
        #             break
        #         index = i
        #     mins.insert(index, number)
        #     mins.pop()
            
        #     index = 3
        #     for i in range(2, -1, -1):
        #         if number < maxs[i]:
        #             break
        #         index = i
        #     maxs.insert(index, number)
        #     maxs.pop()
    
        # maxs = maxs[::-1]

        # # case 1 - first 2 nums
        # result = maxs[-1] - mins[2]

        # # case 2 - last 2 nums
        # result = min(maxs[0] - mins[0], result)

        # # case 3 - first and last number in nums
        # result = min(result, maxs[-2] - mins[1])
        # return result

        # time: O(n)
        # space: O(1)
        # method: greedy

        maxs = heapq.nlargest(3, nums)
        mins = heapq.nsmallest(3, nums)
        maxs = maxs[::-1]
        
        # case 1 - first 2 nums
        result = maxs[-1] - mins[2]

        # case 2 - last 2 nums
        result = min(maxs[0] - mins[0], result)

        # case 3 - first and last number in nums
        result = min(result, maxs[-2] - mins[1])
        return result