class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for i in range(k):
            gain = happiness[i] - i
            if gain <= 0:
                return res
            res += gain
        return res