class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        cur = sum(calories[:k])
        res = int(upper < cur) - int(cur < lower)
        for i in range(k, len(calories)):
            cur += calories[i] - calories[i - k]
            res += int(upper < cur) - int(cur < lower)
        return res