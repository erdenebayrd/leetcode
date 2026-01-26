class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        previousMinimumPrice = float('inf')
        for i in range(len(prices)):
            answer = max(answer, prices[i] - previousMinimumPrice)
            previousMinimumPrice = min(previousMinimumPrice, prices[i])
        return answer