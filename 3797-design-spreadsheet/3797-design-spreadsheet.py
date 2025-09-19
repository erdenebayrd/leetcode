class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = {}

    def initCell(self, cell: str) -> [str, str]:
        col = str(cell[0])
        row = str(cell[1:])
        if row not in self.cells:
            self.cells[row] = {}
        if col not in self.cells[row]:
            self.cells[row][col] = 0
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.initCell(cell)
        self.cells[row][col] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def isCell(self, x: str) -> bool:
        return "A" <= x[0] <= "Z"

    def getCellValue(self, cell: str) -> int:
        row, col = self.initCell(cell)
        return self.cells[row][col]

    def getValue(self, formula: str) -> int:
        res = 0
        for x in formula.replace("=", "").split("+"):
            if self.isCell(x) is True:
                x = self.getCellValue(x)
            else:
                x = int(x)
            res += x
        return res


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)