class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [node for node in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def findParent(self, node: int) -> int:
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
        else: # if the ranks are same
            self.rank[parentV] += 1
            self.parent[parentU] = self.parent[parentV]
        # self.parent[parentV] = self.parent[parentU]

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        seen = set()
        for word in sentence1:
            seen.add(word)
        for word in sentence2:
            seen.add(word)
        for u, v in similarPairs:
            seen.add(u)
            seen.add(v)
        wordMap = {}
        num = 0
        for word in seen:
            wordMap[word] = num
            num += 1

        m = len(wordMap)

        union = UnionFind(m)
        for u, v in similarPairs:
            u = wordMap[u]
            v = wordMap[v]
            union.connect(u, v)
        
        n = len(sentence1)
        for i in range(n):
            node1 = wordMap[sentence1[i]]
            node2 = wordMap[sentence2[i]]
            parent1 = union.findParent(node1)
            parent2 = union.findParent(node2)
            if parent1 != parent2:
                return False
        return True