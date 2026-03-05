from collections import defaultdict

class Node:
    def __init__(self):
        self.value = 0
        self.children = defaultdict(int) # contains cell address as key, value would be how many edges from current node to it's child
        self.parents = defaultdict(int) # value of dict would be how many edges from parent ("key") to current node

class Excel:
    # time: O(N) N is the total number of graph node / cells in the excel
    # space: O(N)
    # method: graph, DAG (Directed Acyclic Graph) implementation
    def __init__(self, height: int, width: str): # O(N)
        self.graph = {}
        for row in range(1, height + 1):
            for column in range(ord("A"), ord(width) + 1):
                cell = str(chr(column)) + str(row)
                self.graph[cell] = Node()

    def clear(self, cell: str) -> None: # O(E) E is the number of edges
        for child in self.graph[cell].children:
            # child is the cell address of child
            del self.graph[child].parents[cell]
        self.graph[cell].value = 0
        self.graph[cell].children.clear() # deleting all keys/children from current node

    def updateParents(self, cell: int, delta: int) -> None: # O(E) E is the number of edges
        for parent in self.graph[cell].parents:
            self.graph[parent].value += delta * self.graph[cell].parents[parent]
            self.updateParents(parent, delta * self.graph[cell].parents[parent])

    def set(self, row: int, column: str, val: int) -> None: # O(E) E is the number of edges
        cell = column + str(row)
        oldValue = self.graph[cell].value
        self.clear(cell)
        self.graph[cell].value = val
        delta = val - oldValue
        self.updateParents(cell, delta)

    def get(self, row: int, column: str) -> int: # O(1)
        cell = column + str(row)
        return self.graph[cell].value

    def addChild(self, cell: str, childAddress: str) -> None:
        self.graph[cell].value += self.graph[childAddress].value
        self.graph[cell].children[childAddress] += 1
        self.graph[childAddress].parents[cell] += 1

    def addChildren(self, cell: str, address: str) -> None:
        if ":" not in address:
            self.addChild(cell, address)
            return
        start, end = address.split(":")
        startColumn, startRow = start[0], int(start[1:])
        endColumn, endRow = end[0], int(end[1:])
        for row in range(startRow, endRow + 1):
            for column in range(ord(startColumn), ord(endColumn) + 1):
                childAddress = chr(column) + str(row)
                self.addChild(cell, childAddress)

    def sum(self, row: int, column: str, numbers: List[str]) -> int: # O(N + E) N number of nodes, E is the number of edges
        cell = column + str(row)
        oldValue = self.graph[cell].value
        self.clear(cell)
        for address in numbers:
            self.addChildren(cell, address)
        newValue = self.graph[cell].value
        delta = newValue - oldValue
        self.updateParents(cell, delta)
        return newValue


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)