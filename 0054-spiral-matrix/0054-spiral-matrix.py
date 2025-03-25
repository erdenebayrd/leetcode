class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        vis = [[False] * m for _ in range(n)]
        res = []
        def dfs(curx: int, cury: int, direction: str):
            vis[curx][cury] = True
            res.append(matrix[curx][cury])
            if direction == "right":
                if cury + 1 < m and vis[curx][cury + 1] is False:
                    dfs(curx, cury + 1, "right")
                elif curx + 1 < n and vis[curx + 1][cury] is False:
                    dfs(curx + 1, cury, "down")
            elif direction == "down":
                if curx + 1 < n and vis[curx + 1][cury] is False:
                    dfs(curx + 1, cury, "down")
                elif cury - 1 >= 0 and vis[curx][cury - 1] is False:
                    dfs(curx, cury - 1, "left")
            elif direction == "left":
                if cury - 1 >= 0 and vis[curx][cury - 1] is False:
                    dfs(curx, cury - 1, "left")
                elif curx - 1 >= 0 and vis[curx - 1][cury] is False:
                    dfs(curx - 1, cury, "up")
            elif direction == "up":
                if curx - 1 >= 0 and vis[curx - 1][cury] is False:
                    dfs(curx - 1, cury, "up")
                elif cury + 1 < m and vis[curx][cury + 1] is False:
                    dfs(curx, cury + 1, "right")
        
        dfs(0, 0, "right")
        return res