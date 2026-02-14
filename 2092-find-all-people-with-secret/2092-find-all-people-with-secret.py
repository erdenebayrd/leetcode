from collections import defaultdict
from sortedcontainers import SortedDict

class UnionFind:
    def __init__(self) -> None:
        self.parent = {}
    
    def findParent(self, node: int) -> int:
        if node not in self.parent:
            self.parent[node] = node
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def isConnected(self, nodeU: int, nodeV: int) -> bool:
        parentU = self.findParent(nodeU)
        parentV = self.findParent(nodeV)
        return parentU == parentV
    
    def connect(self, nodeU: int, nodeV: int) -> None:
        parentU = self.findParent(nodeU)
        parentV = self.findParent(nodeV)
        if parentU != parentV:
            self.parent[parentU] = parentV

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetingsByTime = SortedDict()
        for nodeU, nodeV, time in meetings:
            if time not in meetingsByTime:
                meetingsByTime[time] = []
            meetingsByTime[time].append([nodeU, nodeV])
        
        pool = set([0, firstPerson]) # people who know the secret

        for time in meetingsByTime:
            unionFind = UnionFind()
            edges = meetingsByTime[time]
            for nodeU, nodeV in edges:
                unionFind.connect(nodeU, nodeV) # union find used for detecting same component of each node or not

            parents = defaultdict(set)
            for nodeU, nodeV in edges:
                parentU = unionFind.findParent(nodeU)
                parentV = unionFind.findParent(nodeV)
                parents[parentU].add(nodeU)
                parents[parentV].add(nodeV)
            
            for parent in parents:
                children = parents[parent]
                if children & pool: # at least one common person
                    pool |= children # extended by children
        
        return list(pool)