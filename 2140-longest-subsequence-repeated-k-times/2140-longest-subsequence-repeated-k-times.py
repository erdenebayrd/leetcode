class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # time: O(joohn evgui ug n worst case deeree 26 ^ 7 which gets TLE)
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