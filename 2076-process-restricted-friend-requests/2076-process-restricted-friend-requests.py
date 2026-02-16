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
            self.parent[parentV] = parentU
        elif self.rank[parentU] < self.rank[parentV]:
            self.parent[parentU] = parentV
        else: # self.rank[parentU] == self.rank[parentV]:
            self.parent[parentU] = parentV
            self.rank[parentV] += 1
    
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        # time: O(N + O(len(requests) * len(restrictions))) => O(N ^ 2)
        pool = UnionFind(n) # O(N)
        result = []
        for u, v in requests: # O(len(requests))
            parentU = pool.findParent(u)
            parentV = pool.findParent(v)
            if parentU > parentV:
                parentV, parentU = parentU, parentV
            restricted = False
            for x, y in restrictions: # O(len(restrictions))
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