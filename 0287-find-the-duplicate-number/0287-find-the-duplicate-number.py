class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: Tortoise and Hare algorithm (Floyd cycle detection algorightm by slow and fast pointer)
        slow = fast = 0
        while slow == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow