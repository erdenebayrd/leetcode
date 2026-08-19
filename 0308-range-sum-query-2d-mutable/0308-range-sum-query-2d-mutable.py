class FenwickTree:
    def __init__(self, matrix: list) -> None:
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.ft = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        for row in range(self.rows):
            for col in range(self.cols):
                self.add(row + 1, col + 1, matrix[row][col])

    def add(self, row: int, col: int, value: int) -> None:
        column = col
        while row <= self.rows:
            col = column
            while col <= self.cols:
                self.ft[row][col] += value
                col += col & -col
            row += row & -row
    
    def query(self, left_row: int, right_row: int, left_col: int, right_col: int) -> int:
        return self.__query(right_row, right_col) - self.__query(right_row, left_col - 1) - self.__query(left_row - 1, right_col) + self.__query(left_row - 1, left_col - 1)
    
    def __query(self, row: int, col: int) -> int:
        result = 0
        column = col
        while row:
            col = column
            while col:
                result += self.ft[row][col]
                col -= col & -col
            row -= row & -row
        return result


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = [row[:] for row in matrix]
        self.fenwick_tree = FenwickTree(matrix)

    def update(self, row: int, col: int, val: int) -> None: # O(log (rows * cols))
        diff = val - self.matrix[row][col]
        self.fenwick_tree.add(row + 1, col + 1, diff)
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: # O(log (rows * cols))
        return self.fenwick_tree.query(row1 + 1, row2 + 1, col1 + 1, col2 + 1)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)