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
            if self.rank[parentU] < self.rank[parentV]:
                self.parent[parentU] = parentV
            elif self.rank[parentU] > self.rank[parentV]:
                self.parent[parentV] = parentU
            else: # self.rank[parentU] == self.rank[parentV]
                self.parent[parentU] = parentV
                self.rank[parentV] += 1

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # time: O(N)
        # space: O(N)
        # method: graph union find disjoint set
        
        def calculateHamming(indices: List[int]) -> int:
            count = defaultdict(int)
            for index in indices:
                count[target[index]] += 1
            for index in indices:
                value = source[index]
                if value in count:
                    count[value] -= 1
                    if count[value] == 0:
                        del count[value]
            return sum(count.values())

        unionFind = UnionFind()
        for a, b in allowedSwaps:
            unionFind.union(a, b)
        groups = defaultdict(list)
        n = len(source)
        for node in range(n):
            parent = unionFind.findParent(node)
            groups[parent].append(node)
        
        # print(groups)
        # print(n)
        # count = defaultdict(int)
        # for i in range(n):
        #     count[target[i]] += 1
        #     count[source[i]] -= 1
        # for key in count:
        #     if count[key] == 0:
        #         continue
        #     print(key, count[key])

        result = 0
        for parent in groups:
            children = groups[parent]
            result += calculateHamming(children)
        return result