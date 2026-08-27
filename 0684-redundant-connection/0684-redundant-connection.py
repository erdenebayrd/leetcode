class UnionFind:
    def __init__(self) -> None:
        self.parent = {}
        self.rank = {}
    
    def find_parent(self, node: int) -> int:
        if node not in self.parent:
            self.parent[node] = node
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
    
    def is_same_set(self, node_u: int, node_v: int) -> bool:
        parent_u = self.find_parent(node_u)
        parent_v = self.find_parent(node_v)
        return parent_u == parent_v
    
    def connect(self, node_u: int, node_v: int) -> None:
        parent_u = self.find_parent(node_u)
        parent_v = self.find_parent(node_v)
        
        if parent_u not in self.rank:
            self.rank[parent_u] = 1
        if parent_v not in self.rank:
            self.rank[parent_v] = 1
        
        if self.rank[parent_u] < self.rank[parent_v]:
            self.parent[parent_u] = parent_v
        elif self.rank[parent_u] > self.rank[parent_v]:
            self.parent[parent_v] = parent_u
        else: # ranks are equal
            self.parent[parent_u] = parent_v
            self.rank[parent_v] += 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # time: O(N)
        # space: O(N)
        # method: Union Find
        uf = UnionFind()
        for u, v in edges:
            if uf.is_same_set(u, v):
                return [u, v]
            uf.connect(u, v)