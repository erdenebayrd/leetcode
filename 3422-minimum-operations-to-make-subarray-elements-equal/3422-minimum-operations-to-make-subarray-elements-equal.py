from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # time: O(N log N)
        # space: O(N)
        # method: sorted list + median
        n = len(nums)
        lowSum, highSum = 0, 0
        low, high = SortedList(), SortedList()
        for i in range(k):
            low.add(nums[i])
            lowSum += nums[i]

        for _ in range(k//2):
            lowSum -= low[-1]
            highSum += low[-1]
            high.add(low[-1])
            low.pop()

        median = low[-1]
        result = median * len(low) - lowSum + highSum - len(high) * median
        for i in range(k, n):
            removeValue = nums[i - k]
            if removeValue in high:
                highSum -= removeValue
                high.discard(removeValue)
                high.add(low[-1])
                highSum += low[-1]
                lowSum -= low[-1]
                low.pop()
            else:
                low.discard(removeValue)
                lowSum -= removeValue
            addValue = nums[i]
            high.add(addValue)
            highSum += addValue
            low.add(high[0])
            lowSum += high[0]
            highSum -= high[0]
            high.discard(high[0])
            median = low[-1]
            result = min(result, median * len(low) - lowSum + highSum - len(high) * median)
        return result
