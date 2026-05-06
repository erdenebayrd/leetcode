class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # time: O(N)
        # space: O(1)
        # method: 2 pointers
        n = len(numbers)
        left, right = 0, n - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                break
        return [left + 1, right + 1]