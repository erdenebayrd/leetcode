class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = float('inf')
        for number in nums:
            current = 0
            for ch in str(number):
                current += int(ch)
            result = min(result, current)
        return result