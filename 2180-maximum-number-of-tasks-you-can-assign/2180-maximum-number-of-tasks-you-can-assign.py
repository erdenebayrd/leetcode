class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # time: O(N * LogN)
        # space: O(1)
        tasks.sort()
        workers.sort()
        n = len(tasks)
        m = len(workers)
        
        def can(k: int) -> bool:
            cur = pills
            sl = SortedList(workers[m - k:])
            for i in range(k - 1, -1, -1):
                if sl[-1] >= tasks[i]:
                    sl.pop()
                else:
                    idx = sl.bisect_left(tasks[i] - strength)
                    if idx == len(sl):
                        return False
                    cur -= 1
                    sl.pop(idx)
            return cur >= 0

        # 5 9
        # 1 5

        # 1 pill 
        # 8 strength

        lo, hi = -1, min(n, m) + 1
        while lo + 1 < hi:
            md = (lo + hi) // 2
            if can(md) is True:
                lo = md
            else:
                hi = md
        return lo