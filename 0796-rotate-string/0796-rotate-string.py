class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # time: O(N + M)
        # space: O(N + M)
        # method: KMP pattern search algo
        if len(s) != len(goal):
            return False
        text = goal + goal
        pattern = s
        n = len(pattern)
        lps = [0] * n
        length = 0

        for i in range(1, n):
            while length > 0 and pattern[length] != pattern[i]:
                length = lps[length - 1]
            if pattern[length] == pattern[i]:
                length += 1
            lps[i] = length
        
        length = 0
        for i in range(len(text)):
            while length > 0 and pattern[length] != text[i]:
                length = lps[length - 1]
            if pattern[length] == text[i]:
                length += 1
            if length == len(pattern):
                return True
        return False