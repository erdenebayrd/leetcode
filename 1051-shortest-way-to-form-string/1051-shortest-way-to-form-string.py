class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n = len(source)
        idx = 0
        res = 0
        while idx < len(target):
            res += 1
            curIdx = idx
            for ch in source:
                if idx < len(target) and ch == target[idx]:
                    idx += 1
            if curIdx == idx:
                break
        if idx < len(target):
            return -1
        return res