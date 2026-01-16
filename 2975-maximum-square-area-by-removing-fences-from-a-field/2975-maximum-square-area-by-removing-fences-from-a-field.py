class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.append(1)
        hFences.append(m)
        hFences.sort()        
        hDist = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                hDist.add(hFences[j] - hFences[i])

        vFences.append(1)
        vFences.append(n)
        vFences.sort()
        vDist = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                vDist.add(vFences[j] - vFences[i])
        
        dist = vDist & hDist
        # print(dist)
        if dist:
            w = max(dist)
            area = (w * w) % (int(1e9 + 7))
            return area
        return -1