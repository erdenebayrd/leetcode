class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sz = len(board)
        for i in range(sz):
            row = set()
            col = set()
            for j in range(sz):
                if "." != board[i][j]:
                    x = int(board[i][j])
                    if x in row or x < 1 or x > 9:
                        return False
                    row.add(x)
                
                if board[j][i] != ".":
                    x = int(board[j][i])
                    if x in col or x < 1 or x > 9:
                        return False
                    col.add(x)
        step = 3
        for row in range(0, sz, step):
            for col in range(0, sz, step):
                seen = set()
                for i in range(row, row + step):
                    for j in range(col, col + step):
                        if board[i][j] == ".":
                            continue
                        x = int(board[i][j])
                        if x in seen or x < 1 or x > 9:
                            return False
                        seen.add(x)
        return True