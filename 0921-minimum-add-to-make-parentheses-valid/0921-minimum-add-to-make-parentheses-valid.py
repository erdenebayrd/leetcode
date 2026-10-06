class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # time: O(N)
        # space: O(1)
        # method: greedy

        result = count_open = 0
        for ch in s:
            if ch == "(":
                count_open += 1
            else:
                if count_open == 0:
                    result += 1
                else:
                    count_open -= 1
        result += count_open
        return result