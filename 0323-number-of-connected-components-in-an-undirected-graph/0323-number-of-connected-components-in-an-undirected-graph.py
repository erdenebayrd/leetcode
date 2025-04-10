class Solution:
    def __init__(self):
        self.parent = []
    
    def init(self, n: int):
        self.parent = [x for x in range(n)]

    def findParent(self, v: int) -> int:
        if v == self.parent[v]:
            return v
        self.parent[v] = self.findParent(self.parent[v])
        return self.parent[v]

    def isSameSet(self, u: int, v: int) -> bool:
        parentU = self.findParent(u)
        parentV = self.findParent(v)
        return parentU == parentV

    def connect(self, u: int, v: int) -> None:
        if self.isSameSet(u, v) is True:
            return
        self.parent[self.findParent(u)] = self.findParent(v)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # method: DSU (Disjoint Union Set)
        self.init(n)
        for u, v in edges:
            self.connect(u, v)
        seen = set()
        for i in range(n):
            seen.add(self.findParent(i))
        return len(seen)