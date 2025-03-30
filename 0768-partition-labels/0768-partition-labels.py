class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        for i, ch in enumerate(s):
            pos[ch] = i
        idx = 0
        i = 0
        res = []
        while i < len(s):
            x = pos[s[i]]
            while idx < len(s) and idx < x:
                idx += 1
                x = max(pos[s[idx]], x)
            res.append(idx - i + 1)
            i = idx + 1
        return res