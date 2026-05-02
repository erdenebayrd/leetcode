class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: DFS
        rows = len(board)
        cols = len(board[0])

        def dfs(row: int, col: int) -> None:
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != 'O':
                return
            board[row][col] = "$"
            for deltaRow, deltaCol in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                dfs(deltaRow + row, deltaCol + col)
        
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)
        
        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)
        
        def replaceCharacter(fromCharacter: str, toCharacter: str) -> None:
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] == fromCharacter:
                        board[row][col] = toCharacter
            
        replaceCharacter("O", "X")
        replaceCharacter("$", "O")