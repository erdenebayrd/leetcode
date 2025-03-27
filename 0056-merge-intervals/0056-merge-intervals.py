class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l, r, idx, n = -1, -1, 0, len(intervals)
        res = []
        while idx < n:
            curL, curR = intervals[idx]
            if l == -1:
                l, r = curL, curR
            else:
                if curL <= r: # overlap
                    r = max(r, curR)
                else:
                    res.append([l, r])
                    l, r = curL, curR
            idx += 1
        if len(res) == 0 or res[-1][0] != l or res[-1][1] != r:
            res.append([l, r])
        return res