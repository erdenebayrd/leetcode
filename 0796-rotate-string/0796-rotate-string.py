class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # time: O(N * M)
        # space: O(N + M)
        # method: string pattern search
        n = len(s)
        m = len(goal)
        if n != m:
            return False
        goal = goal + goal
        return s in goal