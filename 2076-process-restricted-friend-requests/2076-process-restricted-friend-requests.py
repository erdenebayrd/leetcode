class UnionFind:
    def __init__(self, n: int):
        self.parent = [node for node in range(n)]
        self.rank = [0] * n
    
    def findParent(self, node: int) -> int:
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def connect(self, nodeU: int, nodeV: int) -> None:
        parentU = self.findParent(nodeU)
        parentV = self.findParent(nodeV)
        if self.rank[parentU] > self.rank[parentV]:
            self.parent[parentV] = self.parent[parentU]
        elif self.rank[parentU] < self.rank[parentV]:
            self.parent[parentU] = self.parent[parentV]
        else: # self.rank[parentU] == self.rank[parentV]:
            self.parent[parentU] = self.parent[parentV]
            self.rank[parentU] += 1
    
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        pool = UnionFind(n)
        result = []
        for u, v in requests:
            parentU = pool.findParent(u)
            parentV = pool.findParent(v)
            if parentU > parentV:
                parentV, parentU = parentU, parentV
            restricted = False
            for x, y in restrictions:
                parentX = pool.findParent(x)
                parentY = pool.findParent(y)
                if parentX > parentY:
                    parentY, parentX = parentX, parentY
                if parentX == parentU and parentY == parentV:
                    restricted = True
                    break
            if restricted:
                result.append(False)
            else:
                result.append(True)
                pool.connect(u, v)
        return result