from sortedcontainers import SortedList

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        sl = SortedList([])
        n = len(classes)
        for p, t in classes:
            diff = (p + 1) / (t + 1) - p / t
            sl.add([diff, p, t])
        while extraStudents > 0:
            extraStudents -= 1
            diff, p, t = sl[-1]
            sl.pop(-1)
            p += 1
            t += 1
            sl.add([(p + 1) / (t + 1) - p / t, p, t])
        res = 0
        for _, p, t in sl:
            res += p / t
        return res / n