class UnionFindDisjointSet:
    def __init__(self):
        self.parent = {}
    
    def findParent(self, node: int):
        if node not in self.parent:
            self.parent[node] = node
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def union(self, nodeX: int, nodeY: int) -> None:
        parentX = self.findParent(nodeX)
        parentY = self.findParent(nodeY)
        if parentX == parentY:
            return
        self.parent[parentX] = self.parent[parentY]

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secret = set([0, firstPerson])
        meetings.sort(key=lambda m: m[2]) # sort by time
        meets = {}
        for x, y, time in meetings:
            if time not in meets:
                meets[time] = []
            meets[time].append([x, y])
        
        for time in meets:
            localPool = UnionFindDisjointSet()
            users = set()
            for x, y in meets[time]:
                localPool.union(x, y)
                users.add(x)
                users.add(y)
            parents = {}
            for user in users:
                parent = localPool.findParent(user)
                if parent not in parents:
                    parents[parent] = set()
                parents[parent].add(user)
            for parent in parents:
                if any([user in secret for user in parents[parent]]):
                    secret.update(parents[parent])
        return list(secret)