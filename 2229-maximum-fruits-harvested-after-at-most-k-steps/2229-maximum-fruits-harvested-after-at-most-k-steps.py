class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        add = 0
        fruits.append([-1, 0])
        fruits.append([int(2e5 + 1), 0])
        for i in range(len(fruits)):
            if fruits[i][0] == startPos:
                add += fruits[i][1]
                fruits[i][1] = 0
        if add == 0:
            fruits.append([startPos, 0])
        fruits.sort()
        n = len(fruits)
        startPosIdx = -1
        for i in range(n):
            if startPos == fruits[i][0]:
                startPosIdx = i
        assert startPosIdx != -1
        # print(startPosIdx)
        # print(fruits)
        prefix = [0] * n
        prefix[0] = fruits[0][1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + fruits[i][1]
        
        def rangeSum(l: int, r: int) -> int:
            if l == 0:
                return prefix[r]
            return prefix[r] - prefix[l - 1]
        
        res = 0
        for i in range(n):
            cur = 0
            pos, amount = fruits[i]
            if pos < startPos:
                if startPos - pos <= k:
                    cur = rangeSum(i, startPosIdx)
                    curK = k - 2 * (startPos - pos)
                    if curK > 0:
                        lo, hi = startPosIdx, n
                        while lo + 1 < hi:
                            md = (lo + hi) // 2
                            if fruits[md][0] - startPos <= curK:
                                lo = md
                            else:
                                hi = md
                        cur += rangeSum(startPosIdx, lo)
            elif startPos < pos:
                if pos - startPos <= k:
                    cur = rangeSum(startPosIdx, i)
                    curK = k - 2 * (pos - startPos)
                    if curK > 0:
                        lo, hi = -1, startPosIdx
                        while lo + 1 < hi:
                            md = (lo + hi) // 2
                            if startPos - fruits[md][0] <= curK:
                                hi = md
                            else:
                                lo = md
                        cur += rangeSum(hi, startPosIdx)
            res = max(res, cur)
        return res + add