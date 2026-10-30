class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # time: O((n + q) * log n)
        # space: O(n * log n)
        # method: lca + fenwick tree + euler tour (dfs) + bitmask
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        left = [-1] * n
        right = [-1] * n
        preorder = []
        parents = [[0] * n.bit_length() for _ in range(n)]
        levels = [0] * n
        values = [0] * n

        def dfs(node: int, parent: int, level: int) -> None:
            parents[node][0] = parent
            levels[node] = level
            preorder.append(node)
            left[node] = len(preorder)
            for child in tree[node]:
                if child == parent:
                    continue
                dfs(child, node, level + 1)

            right[node] = len(preorder)

        dfs(0, -1, 0)

        for level in range(1, n.bit_length()):
            for i in range(n):
                parents[i][level] = parents[parents[i][level - 1]][level - 1]

        def lca(u: int, v: int) -> int:
            while levels[u] != levels[v]:
                diff = abs(levels[u] - levels[v])
                level = diff.bit_length() - 1
                if levels[u] > levels[v]:
                    u = parents[u][level]
                else:
                    v = parents[v][level]
            
            if u == v:
                return v
            
            for level in range(n.bit_length() - 1, -1, -1):
                if parents[u][level] != parents[v][level]:
                    u = parents[u][level]
                    v = parents[v][level]
            
            return parents[v][0]

        ft = [0] * (n + 1) # BIT/Fenwick tree

        def add(index: int, value: int) -> None:
            while index <= n:
                ft[index] ^= value
                index += -index & index
        
        def query(index: int) -> int:
            value = 0
            while index > 0:
                value ^= ft[index]
                index -= -index & index
            return value
        
        for i in range(n):
            pos = ord(s[i]) - ord('a')
            value = 1 << pos
            add(left[i], value)
            add(right[i] + 1, value) # minus
            values[i] = value

        result = []
        for i in range(len(queries)):
            current_query = queries[i].split()
            if current_query[0] == "update":
                u, ch = current_query[1:]
                u = int(u)
                pos = ord(ch) - ord('a')
                value = values[u] ^ (1 << pos)
                values[u] ^= value
                add(left[u], value)
                add(right[u] + 1, value)
            else: # query
                u, v = current_query[1:]
                u, v = int(u), int(v)
                w = lca(u, v)
                value = query(left[u]) ^ query(left[v]) ^ values[w]
                value -= -value & value
                result.append(value == 0)
        
        return result