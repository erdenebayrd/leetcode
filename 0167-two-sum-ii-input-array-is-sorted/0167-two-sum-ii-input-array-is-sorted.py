class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # time: O(N)
        # # space: O(N)
        # seen = {}
        # result = [] # indexes
        # for i in range(len(numbers)):
        #     need = target - numbers[i]
        #     if need in seen:
        #         return [seen[need] + 1, i + 1]
        #     seen[numbers[i]] = i
        # return [-1, -1]

        # O(N * Log N)
        # O(1)
        # for index in range(len(numbers)):
        #     need = target - numbers[index]
        #     low, high = index, len(numbers)
        #     while low + 1 < high:
        #         middle = (low + high) // 2
        #         if numbers[middle] < need:
        #             low = middle
        #         elif numbers[middle] > need:
        #             high = middle
        #         else: # numbers[middle] == need:
        #             return [index + 1, middle + 1]
        # return [-1, -1]

        # O(N)
        # O(1)
        #            [1, 3, 4, 10] target = 7
        # left.          ^
        # right             ^
        # sum = 5 
        # sum < target
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else: # total == target
                return [left + 1, right + 1]
        return [-1, -1]