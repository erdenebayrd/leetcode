class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: simulation
        rows = len(grid)
        cols = len(grid[0])
        layers = []
        row, col = 0, 0
        rowLimit, colLimit = rows - 1, cols - 1
        while row < rows // 2 and col < cols // 2:
            layer = []
            for currow in range(row, rowLimit + 1):
                layer.append(grid[currow][col])
            for curcol in range(col + 1, colLimit + 1):
                layer.append(grid[rowLimit][curcol])
            for currow in range(rowLimit - 1, row - 1, -1):
                layer.append(grid[currow][colLimit])
            for curcol in range(colLimit - 1, col, -1):
                layer.append(grid[row][curcol])
            layers.append(layer)
            row += 1
            col += 1
            rowLimit -= 1
            colLimit -= 1
        
        rotated = []
        for layer in layers:
            shift = k % len(layer)
            start = len(layer) - shift
            rotated.append(layer[start:] + layer[:start])
        
        row, col = 0, 0
        rowLimit, colLimit = rows - 1, cols - 1
        for layer in rotated:
            index = 0
            for currow in range(row, rowLimit + 1):
                grid[currow][col] = layer[index]
                index += 1
            for curcol in range(col + 1, colLimit + 1):
                grid[rowLimit][curcol] = layer[index]
                index += 1
            for currow in range(rowLimit - 1, row - 1, -1):
                grid[currow][colLimit] = layer[index]
                index += 1
            for curcol in range(colLimit - 1, col, -1):
                grid[row][curcol] = layer[index]
                index += 1
            row += 1
            col += 1
            rowLimit -= 1
            colLimit -= 1
        return grid