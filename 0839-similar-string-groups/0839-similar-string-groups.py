class UnionFind:
    def __init__(self) -> None:
        self.parent = {}
        self.rank = {}
    
    def findParent(self, node: int) -> int:
        if node not in self.parent:
            self.parent[node] = node
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def union(self, nodeU: int, nodeV: int) -> None:
        parentU = self.findParent(nodeU)
        parentV = self.findParent(nodeV)
        if parentU not in self.rank:
            self.rank[parentU] = 1
        if parentV not in self.rank:
            self.rank[parentV] = 1

        if parentU != parentV:
            if self.rank[parentU] > self.rank[parentV]:
                self.parent[parentV] = parentU
            elif self.rank[parentU] < self.rank[parentV]:
                self.parent[parentU] = parentV
            else: # tie on rank
                self.parent[parentU] = parentV
                self.rank[parentV] += 1

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # time: O(m * n ^ 2)
        # space: O(n)
        # method: union find + brute force
        n = len(strs)
        m = len(strs[0])        
        unionFind = UnionFind() # initialising union find object
        
        def distance(index1: int, index2: int) -> int:
            cost = 0
            for i in range(m):
                if strs[index1][i] != strs[index2][i]:
                    cost += 1
            return cost
        
        for i in range(n):
            for j in range(i + 1, n):
                if distance(i, j) <= 2:
                    unionFind.union(i, j)
        
        parents = set()
        for i in range(n):
            parent = unionFind.findParent(i)
            parents.add(parent)
        return len(parents)