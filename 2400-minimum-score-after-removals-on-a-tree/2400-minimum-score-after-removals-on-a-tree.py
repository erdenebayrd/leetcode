class Helper:
    def __init__(self, root: int, edges: List[List[int]], nums: List[int]) -> None:
        self.n = len(nums)
        self.nums = nums
        self.root = root
        self.levels = [-1] * self.n
        self.xor = [0] * self.n
        self.adj = [[] for _ in range(self.n)]
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        self.parents = [[-1 for _ in range(11)] for _ in range(self.n)]
        self.dfs(self.root, 0, -1)
        self.initLCA()
        self.initXOR(self.root, -1)
        # print(self.levels)
        # print(self.parents)

    def initXOR(self, cur: int, parent: int) -> None:
        self.xor[cur] = self.nums[cur]
        for child in self.adj[cur]:
            if child == parent:
                continue
            self.initXOR(child, cur)
            self.xor[cur] ^= self.xor[child]

    def dfs(self, cur: int, deep: int, parent: int) -> None:
        self.levels[cur] = deep
        self.parents[cur][0] = parent
        for child in self.adj[cur]:
            if child == parent:
                continue
            self.dfs(child, deep + 1, cur)
        
    def initLCA(self) -> None:
        for parentLevel in range(1, 11):
            for node in range(self.n):
                prevParent = self.parents[node][parentLevel - 1]
                if prevParent == -1:
                    continue
                self.parents[node][parentLevel] = self.parents[prevParent][parentLevel - 1]

    def getLCA(self, u: int, v: int) -> int:
        if self.levels[u] > self.levels[v]: # swap
            w = u
            u = v
            v = w

        while self.levels[u] != self.levels[v]:
            diff = self.levels[v] - self.levels[u]
            parentLevel = int(log(diff, 2))
            v = self.parents[v][parentLevel]
        
        if u == v:
            return v
        
        while self.parents[u][0] != self.parents[v][0]:
            for i in range(10, -1, -1):
                if self.parents[u][i] != self.parents[v][i]:
                    u = self.parents[u][i]
                    v = self.parents[v][i]
                    break
        return self.parents[v][0]
    
    def getDiff(self, u: int, v: int) -> int:
        if self.levels[u] > self.levels[v]:
            w = u
            u = v
            v = w
        uXor = self.xor[u]
        vXor = self.xor[v]
        totalXor = self.xor[self.root]
        if self.getLCA(u, v) == u: # subtree U contains V
            arr = [totalXor ^ uXor, uXor ^ vXor, vXor]    
        else: # U and V are not included each other
            arr = [totalXor ^ uXor ^ vXor, uXor, vXor]
        return max(arr) - min(arr)


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        m = len(edges)
        root = 0
        helper = Helper(root, edges, nums)
        # print(helper.xor)
        res = int(1e8)
        for i in range(m):
            u, v = edges[i]
            if helper.levels[u] < helper.levels[v]:
                u = v
            for j in range(i + 1, m):
                v, w = edges[j]
                if helper.levels[v] < helper.levels[w]:
                    v = w
                res = min(res, helper.getDiff(u, v))
        return res