class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reversedNumber(number: int) -> int:
            result = 0
            while number:
                result = result * 10 + number % 10
                number //= 10
            return result
        return abs(reversedNumber(n) - n)