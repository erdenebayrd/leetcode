class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        pos = {}
        for idx, color in enumerate(colors):
            if color not in pos:
                pos[color] = []
            pos[color].append(idx)
        res = []
        for idx, color in queries:
            if color not in pos:
                res.append(-1)
            else:
                index = bisect.bisect_left(pos[color], idx)
                if index >= len(pos[color]):
                    res.append(abs(pos[color][index - 1] - idx))
                elif index == 0:
                    res.append(abs(pos[color][index] - idx))
                else:
                    res.append(abs(pos[color][index] - idx))
                    res[-1] = min(res[-1], abs(pos[color][index - 1] - idx))
        return res