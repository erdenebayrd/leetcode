class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [node for node in range(n + 1)]
        self.rank = [1] * (n + 1) # how many children do you have? "rank"
    
    def findParent(self, node: int) -> int:
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def connect(self, nodeU: int, nodeV: int) -> None:
        parentU = self.findParent(nodeU)
        parentV = self.findParent(nodeV)
        if parentU == parentV:
            return
        if self.rank[parentU] > self.rank[parentV]:
            self.parent[parentV] = self.parent[parentU]
        elif self.rank[parentU] < self.rank[parentV]:
            self.parent[parentU] = self.parent[parentV]
        else: # self.rank[parentU] == self.rank[parentV]
            self.parent[parentV] = self.parent[parentU]
            self.rank[parentU] += 1
    
    def isConnected(self, nodeU: int, nodeV: int) -> bool:
        parentU = self.findParent(nodeU)
        parentV = self.findParent(nodeV)
        return parentU == parentV
    
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        # time: O(N * Log (N) + len(queries))
        # space: O(N)
        pool = UnionFind(n)
        for node in range(threshold + 1, n + 1): # harmonic series # O(N * log N) but pool.connect requires Log N but with the rank optimization it's nearly O(1)
            for neighbor in range(2 * node, n + 1, node):
                pool.connect(node, neighbor)
        
        result = []
        for nodeU, nodeV in queries:
            connected = pool.isConnected(nodeU, nodeV)
            result.append(connected)
        
        return result