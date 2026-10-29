class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b); g[b].append(a)

        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        letter = [1 << (ord(c) - 97) for c in s]

        # DFS without recursion: Euler tour times, parent, depth
        t = 0
        stack = [(0, 0, False)]
        seen = [False] * n
        while stack:
            u, p, done = stack.pop()
            if done:
                tout[u] = t - 1
                continue
            seen[u] = True
            up[0][u] = p
            tin[u] = t; t += 1
            stack.append((u, p, True))
            for v in g[u]:
                if not seen[v]:
                    depth[v] = depth[u] + 1
                    stack.append((v, u, False))
        for k in range(1, LOG):
            prev, cur = up[k - 1], up[k]
            for v in range(n):
                cur[v] = prev[prev[v]]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            d = depth[a] - depth[b]
            k = 0
            while d:
                if d & 1:
                    a = up[k][a]
                d >>= 1; k += 1
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]; b = up[k][b]
            return up[0][a]

        # Fenwick tree: XOR on a range, read one point
        tree = [0] * (n + 2)
        def add(i, x):
            i += 1
            while i <= n + 1:
                tree[i] ^= x
                i += i & -i
        def point(i):
            i += 1; r = 0
            while i > 0:
                r ^= tree[i]
                i -= i & -i
            return r
        def subtree_xor(u, x):
            add(tin[u], x)
            add(tout[u] + 1, x)

        for u in range(n):
            subtree_xor(u, letter[u])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1]); nb = 1 << (ord(parts[2]) - 97)
                subtree_xor(u, letter[u] ^ nb)
                letter[u] = nb
            else:
                u, v = int(parts[1]), int(parts[2])
                m = point(tin[u]) ^ point(tin[v]) ^ letter[lca(u, v)]
                ans.append(m & (m - 1) == 0)
        return ans