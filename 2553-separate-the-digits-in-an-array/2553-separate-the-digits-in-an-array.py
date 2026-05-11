class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # time: O(N log maxValue)
        # space: O(N log maxValue)
        # method: do what it says
        def digits(number: int) -> List[int]:
            result = []
            while number:
                result.append(number % 10)
                number //= 10
            result = result[::-1]
            return result
        
        result = []
        for number in nums:
            result.extend(digits(number))
        return result