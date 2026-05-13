from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        so the good sub array (continious) is good if number of distinct values equal to k (exactly)

        what we can do is count how many continious subarray at most k distinct integers which ends at index "right"
        we can calculate this with O(N) time using sliding window method

        starting from left (0'th index) to go to right direction until length of given array (nums)

        but when our window contains more than k distinct values
        we can reduce our window from left -> right until at most k distinct values included in current window

        now, lets say we imagine we already have at_most(limit) function
        which gives us number of continious subarray with at most "limit" distinct integers 

        but we need to count exactly k distinct integers continious subarray

        so, we can just do 
        at_most(k) which gives us a number of subarrays with at most k distinct integers
        at_most(k - 1) which gives us a number of subarrays with at most k - 1 distinct integers

        we can at_most(k) - at_most(k - 1) is saying how many subarray with exactly k number of subarrays we have

        which is the number of good subarrays
        """
        # time: O(N)
        # space: O(N) due to hash map to count distinct integers
        # method: kinda combinatoric

        def at_most(limit: int) -> int:
            frequency = defaultdict(int)
            left = 0
            result = 0
            for right in range(len(nums)):
                frequency[nums[right]] += 1
                while len(frequency) > limit:
                    frequency[nums[left]] -= 1
                    if frequency[nums[left]] == 0:
                        del frequency[nums[left]]
                    left += 1
                result += right - left + 1
            return result
        
        result = at_most(k) - at_most(k - 1)
        return result