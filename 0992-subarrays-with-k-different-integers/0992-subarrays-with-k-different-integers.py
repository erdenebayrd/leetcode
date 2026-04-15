class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # time: O(N)
        # space: O(N)
        # method: sliding window + COUNTING (which is the most important one)
        def atMost(distinctCountLimit: int) -> int:
            left = 0
            count = defaultdict(int)
            currentDistinctCount = 0
            result = 0
            for right in range(len(nums)):
                count[nums[right]] += 1
                if count[nums[right]] == 1:
                    currentDistinctCount += 1
                while left <= right and currentDistinctCount > distinctCountLimit:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        currentDistinctCount -= 1
                    left += 1
                # meaning end at pointer right, starting from left all subarrays are okay
                result += right - left + 1
            return result
        result = atMost(k) - atMost(k - 1)
        return result