from collections import defaultdict
from sortedcontainers import SortedDict

class UnionFind:
    def __init__(self) -> None:
        self.parent = {}
        self.rank = defaultdict(int)
    
    def findParent(self, node: int) -> int:
        if node not in self.parent:
            self.parent[node] = node
        if self.parent[node] == node:
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
            self.rank[parentV] += 1
            self.parent[parentU] = self.parent[parentV]

        # if parentU != parentV:
        #     self.parent[parentU] = parentV

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # time: O(M * Log M + N) M is number of meetings, N is n
        # space: O(M + N)
        meetingsByTime = defaultdict(list)
        for nodeU, nodeV, time in meetings:
            meetingsByTime[time].append([nodeU, nodeV])
        
        pool = set([0, firstPerson]) # people who know the secret

        for time in sorted(meetingsByTime):
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