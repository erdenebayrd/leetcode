class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        prev = float('-inf')

        def calculate(left, right):
            if left > right:
                return None
            left = max(left, lower)
            right = min(right, upper)
            if left > right:
                return None
            return [left, right]

        for number in nums:
            missed = calculate(prev + 1, number - 1)
            prev = number
            if missed is not None:
                result.append(missed)
        missed = calculate(prev + 1, upper)
        if missed is not None:
            result.append(missed)
        return result