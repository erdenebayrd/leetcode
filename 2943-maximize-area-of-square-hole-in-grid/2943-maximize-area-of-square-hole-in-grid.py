class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        lch = 1
        cur = 1
        for i in range(1, len(hBars)):
            if hBars[i - 1] + 1 == hBars[i]:
                cur += 1
            else:
                cur = 1
            lch = max(lch, cur)
        lcv = 1
        cur = 1
        for i in range(1, len(vBars)):
            if vBars[i - 1] + 1 == vBars[i]:
                cur += 1
            else:
                cur = 1
            lcv = max(lcv, cur)
        w = min(lcv, lch) + 1
        return w * w