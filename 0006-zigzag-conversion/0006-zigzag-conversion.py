class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        """
            0 1 2 1 0 1 2 1 0 1 2 1 0 1
            P A Y P A L I S H I R I N G
        """
        if numRows == 1:
            return s
        n = len(s)
        rows = [0] * n
        delta = 1
        for i in range(1, n):
            if rows[i - 1] == 0:
                delta = 1
            if rows[i - 1] == numRows - 1:
                delta = -1
            rows[i] = rows[i - 1] + delta
        zigzag = [[] for _ in range(numRows)]
        for i in range(n):
            row = rows[i]
            zigzag[row].append(s[i])
        
        result = ""
        for row in range(numRows):
            result += "".join(zigzag[row])
        return result