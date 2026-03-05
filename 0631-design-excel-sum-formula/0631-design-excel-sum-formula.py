"""
Design the basic function of Excel and implement the function of the sum
formula.

Implement the Excel class:
- Excel(int height, char width) Initializes the object with the height and the
width of the sheet. The sheet is an integer matrix mat of size height x width
with all values initially 0. A cell referenced as (row, column) where row is in
[1, height] and column is in ['A', width].
- void set(int row, char column, int val) Changes the value at mat[row][column]
to be val.
- int get(int row, char column) Returns the value at mat[row][column].
- int sum(int row, char column, List<String> numbers) Sets the value at
mat[row][column] to be the sum of cells represented by numbers and returns the
value. numbers[i] could be "ColRow" for a single cell or "ColRow1:ColRow2" for a
range of cells.

Example:
Input: ["Excel","set","sum","set","get"]
       [
  [3,"C"],
  [1,"A",2],
  [3,"C",["A1","A1:B2"],
  [2,"B",2],
  [3,"C"]]
Output: [null,null,4,null,6]

Constraints:
- 1 <= height <= 26
- 'A' <= width <= 'Z]
]
"""

class Node:
    def __init__(self) -> None:
        self.value = 0
        self.children = [] # since sum is a list of refereces, same node can be contained more than 1 as a child
        self.parents = {} # current node's parent will be contained here as key, value is how many edges from parent to current node

class Excel:
    def __init__(self, height: int, width: str):
        self.graph = {}
        for row in range(1, height + 1):
            for col in range(ord('A'), ord(width) + 1):
                cell = chr(col) + str(row)
                self.graph[cell] = Node()

    def updateParentValues(self, cell: str, delta: int) -> None:
        for parent in self.graph[cell].parents:
            edges = self.graph[cell].parents[parent]
            self.graph[parent].value += edges * delta
            self.updateParentValues(parent, edges * delta)

    def updateChildren(self, cell: str) -> None:
        for child in self.graph[cell].children: # removing connections from parent node of each child
            if cell in self.graph[child].parents:
                del self.graph[child].parents[cell]
        self.graph[cell].children.clear() # removing connections from children nodes

    def set(self, row: int, column: str, val: int) -> None:
        cell = column + str(row)
        self.updateChildren(cell)
        oldValue = self.graph[cell].value
        self.graph[cell].value = val
        delta = val - oldValue
        self.updateParentValues(cell, delta)

    def get(self, row: int, column: str) -> int:
        cell = column + str(row)
        return self.graph[cell].value

    def updateCell(self, cell: str, cells: list[str]) -> None:
        oldValue = self.graph[cell].value
        for child in cells:
            self.graph[cell].value += self.graph[child].value
            self.graph[cell].children.append(child)
            if cell not in self.graph[child].parents:
                self.graph[child].parents[cell] = 0
            self.graph[child].parents[cell] += 1
        newValue = self.graph[cell].value
        delta = newValue - oldValue
        self.updateParentValues(cell, delta)

    def sum(self, row: int, column: str, numbers: list[str]) -> int:
        cell = column + str(row)
        self.set(row, column, 0)
        cells = []
        for number in numbers:
            if ":" not in number: # menaing only one cell
                cells.append(number)
            else: # range of cells
                start, end = number.split(":") # A1:B2
                colStart = start[0]
                rowStart = int(start[1:])
                colEnd = end[0]
                rowEnd = int(end[1:])
                for rowCurrent in range(rowStart, rowEnd + 1):
                    for colCurrent in range(ord(colStart), ord(colEnd) + 1):
                        cellCurrent = chr(colCurrent) + str(rowCurrent)
                        cells.append(cellCurrent)
        self.updateCell(cell, cells)
        return self.graph[cell].value