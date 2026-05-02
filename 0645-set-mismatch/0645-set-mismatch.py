class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # time: O(N)
        # space: O(1)
        # method: xor
        n = len(nums)
        xor = 0
        for i in range(1, n + 1):
            xor ^= i ^ nums[i - 1]
        
        bit = xor & -xor
        left, right = 0, 0
        for i in range(1, n + 1):
            if bit & i:
                left ^= i
            else:
                right ^= i
            
            if bit & nums[i - 1]:
                left ^= nums[i - 1]
            else:
                right ^= nums[i - 1]
        
        for i in range(n):
            if nums[i] == right:
                left, right = right, left
                break
        return [left, right]