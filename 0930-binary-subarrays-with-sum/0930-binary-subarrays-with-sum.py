class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # # time: O(N)
        # # space: O(N)
        # # method: DP
        # count = defaultdict(int)
        # count[0] = 1
        # n = len(nums)
        # prefix = [0] * n
        # prefix[0] = nums[0]
        # for i in range(1, n):
        #     prefix[i] = prefix[i - 1] + nums[i]
        
        # result = 0
        # for i in range(n):
        #     # prefix[i] - x == goal
        #     need = prefix[i] - goal
        #     result += count[need]
        #     count[prefix[i]] += 1
        # return result

        # time: O(N)
        # space: O(1)
        # method: 2 pointers + atMost
        n = len(nums)
        def atMost(limit: int) -> int:
            left = 0
            currentSum = 0
            result = 0
            for right in range(n):
                currentSum += nums[right]
                while left <= right and currentSum > limit:
                    currentSum -= nums[left]
                    left += 1
                result += (right - left + 1)
            return result
        
        result = atMost(goal) - atMost(goal - 1)
        return result