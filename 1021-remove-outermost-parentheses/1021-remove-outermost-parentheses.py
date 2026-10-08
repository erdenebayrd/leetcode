class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        current_level = 0
        result = []
        for ch in s:
            if ch == "(":
                current_level += 1
                if current_level > 1:
                    result.append(ch)
            else:
                current_level -= 1
                if current_level > 0:
                    result.append(ch)
        return "".join(result)