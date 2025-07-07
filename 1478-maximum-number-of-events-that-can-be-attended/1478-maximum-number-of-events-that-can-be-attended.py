class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        sl = SortedList([x for x in range(1, int(1e5 + 1))])
        res = 0
        for st, ed in events:
            if not sl:
                continue
            idx = sl.bisect_left(st)
            if idx >= len(sl) or sl[idx] > ed:
                continue
            sl.pop(idx)
            res += 1
        return res