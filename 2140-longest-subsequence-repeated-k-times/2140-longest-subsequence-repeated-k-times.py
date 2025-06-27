class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        candidates = sorted([ch for ch, cnt in Counter(s).items() if cnt >= k], reverse=True)
        # print(candidates)
        res = ""
        queue = deque(candidates)
        while queue:
            cur = queue.popleft()
            if len(res) < len(cur):
                res = cur
            for ch in candidates:
                nxt = cur + ch
                it = iter(s)
                if all([ch in it for ch in nxt * k]):
                    queue.append(nxt)

        return res