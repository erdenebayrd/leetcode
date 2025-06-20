class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = 0
        cnt = defaultdict(int)
        for ch in s:
            cnt[ch] += 1
            cur = max(cnt["N"], cnt["S"]) - min(cnt["N"], cnt["S"])
            cur += max(cnt["E"], cnt["W"]) - min(cnt["E"], cnt["W"])
            diff = min(cnt["N"], cnt["S"]) + min(cnt["E"], cnt["W"])
            cur += 2 * min(diff, k)
            res = max(res, cur)
        return res