class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # time: O(N)
        # space: O(N)
        seen = {}
        result = [] # indexes
        for i in range(len(numbers)):
            need = target - numbers[i]
            if need in seen:
                return [seen[need] + 1, i + 1]
            seen[numbers[i]] = i
        return [-1, -1]