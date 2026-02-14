class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # time: O(N)
        # space: O(N)

        n = len(nums)
        evens = [0] * n
        odds = [0] * n
        for index in range(n):
            nums[index] = nums[index] & 1 # 1 if odd number, otherwise 0
            evens[index] = nums[index] ^ 1 # 1 if even, otherwhise 0
            odds[index] = nums[index]

        for index in range(1, n):
            nums[index] += nums[index - 1]

        evensPrefix = [0] * n
        evensPrefix[0] = evens[0]
        for index in range(1, n):
            evensPrefix[index] = evens[index]
            if evens[index] == 0 or evens[index - 1] == 0:
                continue
            evensPrefix[index] += evensPrefix[index - 1]

        evensSuffix = [0] * n
        evensSuffix[n - 1] = evens[n - 1]
        for index in range(n - 2, -1, -1):
            evensSuffix[index] = evens[index]
            if evens[index] == 0 or evens[index + 1] == 0:
                continue
            evensSuffix[index] += evensSuffix[index + 1]

        # print(nums)
        # print(evens)
        # print(evensPrefix)
        # print(evensSuffix)

        def getRangeSum(left: int, right: int) -> int:
            if left == 0:
                return nums[right]
            return nums[right] - nums[left - 1]

        def countEvenNumbersTillReachOddBefore(index: int) -> int: # O(1)
            if index <= 0:
                return 0
            return evensPrefix[index - 1]
        
        def countEvenNumbersTillReachOddAfter(index: int) -> int: # O(1)
            if index >= n - 1:
                return 0
            return evensSuffix[index + 1]
        
        result = 0
        left = 0
        for right in range(n):
            while left <= right and getRangeSum(left, right) == k:
                left += 1
            if left - 1 >= 0 and getRangeSum(left - 1, right) == k and odds[right] == 1:
                result += (countEvenNumbersTillReachOddBefore(left - 1) + 1) * (countEvenNumbersTillReachOddAfter(right) + 1)
        return result