class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # time: O(N)
        # space: O(1) excluding result array
        # method: simulating

        n = len(nums)
        result = [0] * n
        
        # 2 passes
        result[0] = nums[0]
        result[n - 1] = nums[1]
        left = 0
        right = n - 1
        for i in range(2, n):
            if result[left] > result[right]:
                left += 1
                result[left] = nums[i]
            else:
                right -= 1
                result[right] = nums[i]
        
        # reversing right -> n - 1
        for i in range(right, right + (n - right) // 2):
            result[i], result[n - 1 - i + right] = result[n - 1 - i + right], result[i]
        return result