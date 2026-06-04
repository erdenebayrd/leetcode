class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        result = 0
        for number in range(num1, num2 + 1):
            s = str(number)
            for i in range(1, len(s) - 1):
                _prev = int(s[i - 1])
                _curr = int(s[i])
                _next = int(s[i + 1])
                if _prev < _curr > _next or _prev > _curr < _next:
                    result += 1
        return result