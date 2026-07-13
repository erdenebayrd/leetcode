class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def generate(length: int) -> list:
            nums = []
            for i in range(1, 10):
                candidate = []
                for j in range(i, min(10, i + length)):
                    candidate.append(str(j))
                number = "".join(candidate)
                if len(number) == length:
                    nums.append(number)
            result = []
            for number in nums:
                result.append(int(number))
            return result

        result = []
        for length in range(len(str(low)), len(str(high)) + 1):
            nums = generate(length)
            if not nums:
                break
            for number in nums:
                if low <= number <= high:
                    result.append(number)
        return result