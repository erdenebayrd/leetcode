class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def max_continius_stick(arr: List[int]) -> int:
            assert len(arr) >= 1
            arr.sort()
            res = 1
            cur = 1
            for i in range(1, len(arr)):
                if arr[i - 1] + 1 == arr[i]:
                    cur += 1
                else:
                    cur = 1
                res = max(res, cur)
            return res

        width = max_continius_stick(vBars)
        height = max_continius_stick(hBars)
        area = (min(width, height) + 1) ** 2
        return area