class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # time: O(N)
        # space: O(1)
        # method: counting + 2 pointers
        n = len(nums)
        def atMost(limit: int) -> int:
            left = 0
            countOdd = 0
            countNice = 0
            for right in range(n):
                if nums[right] & 1:
                    countOdd += 1
                while left <= right and countOdd > limit:
                    if nums[left] & 1:
                        countOdd -= 1
                    left += 1
                countNice += right - left + 1
            return countNice
        
        return atMost(k) - atMost(k - 1)