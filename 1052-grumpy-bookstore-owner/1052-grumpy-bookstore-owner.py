class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # time: O(N)
        # space: O(1)
        # method: sliding window
        n = len(customers)

        left_sum = right_sum = window_sum = 0
        for i in range(minutes, n):
            right_sum += customers[i] * (grumpy[i] ^ 1)

        for i in range(minutes):
            window_sum += customers[i]

        result = left_sum + window_sum + right_sum
        for i in range(minutes, n):
            window_sum += customers[i] - customers[i - minutes]
            left_sum += customers[i - minutes] * (grumpy[i - minutes] ^ 1)
            right_sum -= customers[i] * (grumpy[i] ^ 1)
            result = max(result, left_sum + window_sum + right_sum)
        return result