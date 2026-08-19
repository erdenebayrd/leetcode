class UnionFind:
    def __init__(self) -> None:
        self.parent = {}
        self.rank = {}
    
    def find(self, node: int) -> int:
        if node not in self.parent:
            self.parent[node] = node
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def connect(self, node_u: int, node_v: int) -> None:
        parent_u, parent_v = self.find(node_u), self.find(node_v)
        if parent_u == parent_v: # already connected
            return
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
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # time: O(M * log M) M = len(connections)
        # space: O(N)
        # method: Minimum spanning Tree (Kruskal) + UnionFind

        connections.sort(key=lambda x: x[-1])
        result = 0
        dsu = UnionFind()
        for u, v, cost in connections:
            if dsu.find(u) == dsu.find(v):
                continue
            dsu.connect(u, v)
            result += cost
        for node in range(1, n):
            if dsu.find(node) != dsu.find(node + 1):
                return -1
        return result