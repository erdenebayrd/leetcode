class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # time: O(N)
        # space: O(1)
        # method: sliding window
        n = len(customers)
        for i in range(n):
            grumpy[i] ^= 1

        left_sum = right_sum = window_sum = 0
        for i in range(minutes, n):
            right_sum += customers[i] * grumpy[i]

        for i in range(minutes):
            window_sum += customers[i]

        result = left_sum + window_sum + right_sum
        for i in range(minutes, n):
            window_sum += customers[i] - customers[i - minutes]
            left_sum += customers[i - minutes] * grumpy[i - minutes]
            right_sum -= customers[i] * grumpy[i]
            result = max(result, left_sum + window_sum + right_sum)
        return result