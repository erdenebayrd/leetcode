class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]
        n = max(len(v1), len(v2))
        for i in range(min(len(v1), len(v2)), n):
            if i >= len(v1):
                v1.append(0)
            if i >= len(v2):
                v2.append(0)
        for i in range(n):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        return 0