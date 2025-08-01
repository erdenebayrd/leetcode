class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        # time: O(N * Log N)
        # space: O(N)
        # method: smthng + sliding window
        sl = [0, 0]
        m = len(conflictingPairs)
        conflictingPairs = sorted([[l, r] if l < r else [r, l] for l, r in conflictingPairs], key=lambda x: x[1])
        idx = 0
        base = 0
        vote = [0] * (n + 1)
        for r in range(1, n + 1):
            while idx < m and conflictingPairs[idx][1] <= r:
                sl.append(conflictingPairs[idx][0])
                idx += 1
                sl.sort()
                while len(sl) > 2:
                    sl.pop(0)
            base += r - sl[-1]
            vote[sl[-1]] += sl[-1] - sl[-2]
        return base + max(vote)