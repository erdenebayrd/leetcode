class Helper:
    def __init__(self, root: int, edges: List[List[int]], nums: List[int]) -> None:
        self.n = len(nums)
        self.nums = nums
        self.root = root
        self.levels = [-1] * self.n
        self.xor = [0] * self.n
        self.adj = [[] for _ in range(self.n)]
        self.subTreeContains = {}
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        self.dfs(self.root, 0, -1)
        self.initXOR(self.root, -1)

    def initXOR(self, cur: int, parent: int) -> None:
        self.xor[cur] = self.nums[cur]
        for child in self.adj[cur]:
            if child == parent:
                continue
            self.initXOR(child, cur)
            self.xor[cur] ^= self.xor[child]

    def dfs(self, cur: int, deep: int, parent: int) -> List[int]:
        self.levels[cur] = deep
        self.subTreeContains[cur] = {}
        self.subTreeContains[cur][cur] = True
        children = [cur]
        for child in self.adj[cur]:
            if child == parent:
                continue
            curChildren = self.dfs(child, deep + 1, cur)
            for x in curChildren:
                self.subTreeContains[cur][x] = True
            children.extend(curChildren)
        return children

    def getDiff(self, u: int, v: int) -> int:
        if self.levels[u] > self.levels[v]:
            w = u
            u = v
            v = w
        uXor = self.xor[u]
        vXor = self.xor[v]
        totalXor = self.xor[self.root]
        # if self.getLCA(u, v) == u: # subtree U contains V
        if v in self.subTreeContains[u]: # subtree U contains V
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
        # print(helper.subTreeContains)
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