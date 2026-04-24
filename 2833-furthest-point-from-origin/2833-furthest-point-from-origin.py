class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # time: O(N)
        # space: O(1)
        # method: greedy + counting
        countL, countR, countUnderScore = 0, 0, 0
        for move in moves:
            if move == "L":
                countL += 1
            elif move == "R":
                countR += 1
            else:
                countUnderScore += 1
        return max(countL - countR, countR - countL) + countUnderScore