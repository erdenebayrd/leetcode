class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        indices = []
        n = len(s)
        current_level = 0
        levels = [0] * n
        for i in range(n):
            if s[i] == "(":
                current_level += 1
                levels[i] = current_level
            else:
                levels[i] = current_level
                current_level -= 1
        
        result = []
        for i in range(n):
            if levels[i] == 1:
                continue
            result.append(s[i])
        return "".join(result)