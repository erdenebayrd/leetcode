class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        end = [-1] * n
        stack = []
        for i in range(n):
            if stack and s[i] == ')':
                end[stack[-1]] = i
                stack.pop()
            if s[i] == '(':
                stack.append(i)

        def startsFrom(left: int) -> int:
            if left >= n or s[left] == ')':
                return 0
            right = end[left]
            score = 0
            if left + 1 == right:
                score += 1
            else:
                score += getRange(left + 1, right - 1) * 2
            score += startsFrom(right + 1)
            return score
        
        def getRange(left: int, right: int) -> int:
            if left > right:
                return 0
            return startsFrom(left)
        
        return startsFrom(0)