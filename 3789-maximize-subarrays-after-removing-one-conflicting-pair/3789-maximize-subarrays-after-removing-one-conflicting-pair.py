from sortedcontainers import SortedList

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        conflictingPairs = [[l, r] if l < r else [r, l] for l, r in conflictingPairs]
        conflictingPairs.sort(key=lambda x: x[1])
        # print(conflictingPairs)
        # sl = SortedList([])
        sl = [0, 0]
        m = len(conflictingPairs)
        idx = 0
        base = 0
        vote = [0] * (n + 1)
        for r in range(1, n + 1):
            while idx < m and conflictingPairs[idx][1] <= r:
                # sl.add(conflictingPairs[idx][0])
                sl.append(conflictingPairs[idx][0])
                idx += 1
                sl.sort()
                while len(sl) > 2:
                    sl.pop(0)
            base += r - sl[-1]
            vote[sl[-1]] += sl[-1] - sl[-2]
            # if len(sl) == 0:
            #     base += r
            # elif len(sl) == 1:
            #     base += r - sl[-1]
            #     vote[sl[-1]] += sl[-1]
            # else: # len(sl) >= 2
            #     base += r - sl[-1]
            #     vote[sl[-1]] += sl[-1] - sl[-2]
        # print(base)
        # print(vote)
        return base + max(vote)