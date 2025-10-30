class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        pos = {}
        for idx, x in enumerate(target):
            if x not in pos:
                pos[x] = []
            pos[x].append(idx)
        
        inf = int(1e9)
        st = [inf] * 4 * n
        def build(p: int, l: int, r: int) -> None:
            if l == r:
                st[p] = target[r]
                return
            build(2 * p, l, (l + r) // 2)
            build(2 * p + 1, (l + r) // 2 + 1, r)
            st[p] = min(st[2 * p], st[2 * p + 1])
        build(1, 0, n - 1)
        def rmq(p: int, l: int, r: int, L: int, R: int) -> int:
            if l > r or l > R or r < L:
                return inf
            if l >= L and r <= R:
                return st[p]
            return min(rmq(2 * p, l, (l + r) // 2, L, R), rmq(2 * p + 1, (l + r) // 2 + 1, r, L, R))
        
        def solve(l: int, r: int, base: int) -> int:
            if l > r:
                return 0
            mnVal = rmq(1, 0, n - 1, l, r)
            le = bisect.bisect_left(pos[mnVal], l)
            ri = bisect.bisect_right(pos[mnVal], r) - 1
            res = mnVal - base
            res += solve(l, pos[mnVal][le] - 1, mnVal)
            res += solve(pos[mnVal][ri] + 1, r, mnVal)
            for i in range(le, ri):
                res += solve(pos[mnVal][i] + 1, pos[mnVal][i + 1] - 1, mnVal)
            # print(l, r, base, res)
            return res
        
        return solve(0, n - 1, 0)