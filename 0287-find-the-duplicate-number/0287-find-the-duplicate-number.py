class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: Tortoise and Hare algo
        slow = fast = 0
        while slow == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow