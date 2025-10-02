class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # minimum spanning tree
        connections.sort(key=lambda x: x[2])
        parents = [x for x in range(n + 1)]
        
        def findParent(x: int) -> int:
            if x == parents[x]:
                return x
            parents[x] = findParent(parents[x])
            return parents[x]

        def isSameSet(x: int, y: int) -> bool:
            parentX = findParent(x)
            parentY = findParent(y)
            return parentX == parentY
        
        def connect(x: int, y: int) -> None:
            parentX = findParent(x)
            parentY = findParent(y)
            parents[parentX] = parentY
        
        res = 0
        for x, y, cost in connections:
            if isSameSet(x, y) is True:
                continue
            connect(x, y)
            res += cost
        
        parent = findParent(1)
        for i in range(1, n + 1):
            if findParent(i) != parent:
                return -1
        return res