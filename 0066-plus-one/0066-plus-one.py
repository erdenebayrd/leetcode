class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        x = 1
        for i in range(len(digits)):
            digits[i] += x
            x = digits[i] // 10
            digits[i] = digits[i] % 10
        if x != 0:
            digits.append(x)
        return digits[::-1]