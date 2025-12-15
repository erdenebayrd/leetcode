class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        self.n = len(s)
        self.ft = [0] * (self.n + 1) # fenwick tree
        arr = [1 if ch == "A" else 0 for ch in s]
        def update(idx: int, val: int) -> None:
            while idx <= self.n:
                self.ft[idx] += val
                idx += idx & -idx
        
        def query(ri: int) -> int:
            res = 0
            while ri > 0:
                res += self.ft[ri]
                ri -= ri & -ri
            return res

        # init
        for i in range(1, self.n):
            if arr[i] == arr[i - 1]:
                update(i + 1, 1)
        
        res = []
        for i in range(len(queries)):
            if queries[i][0] == 1: # modify query
                idx = queries[i][1]
                arr[idx] ^= 1
                if idx > 0:
                    update(idx + 1, 1 if arr[idx - 1] == arr[idx] else -1)
                if idx < self.n - 1:
                    update(idx + 2, 1 if arr[idx + 1] == arr[idx] else -1)
                continue
            l, r = queries[i][1:]
            res.append(query(r + 1) - query(l + 1))
        return res