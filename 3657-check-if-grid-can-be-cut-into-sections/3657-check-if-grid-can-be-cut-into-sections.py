class Solution:
    def solve(self, edges: List[List[int]]) -> bool:
        edges.sort()
        cntPieces = 0
        l, r = edges[0]
        for i in range(1, len(edges)):
            le, ri = edges[i]
            if le < r: # overlap
                r = max(r, ri)
            else: # separate
                cntPieces += 1
                l, r = le, ri
        return cntPieces >= 2


    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # time: O(N * LogN)
        # space: O(N)
        # method: sliding window
        res = self.solve([[i[0], i[2]] for i in rectangles])
        res |= self.solve([[i[1], i[3]] for i in rectangles])
        return res