class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # time: O(N log N)
        # space: O(1)
        # method: sort + simulation
        n = len(dist)
        for i in range(n):
            dist[i] = dist[i] // speed[i] + int(dist[i] % speed[i] > 0)
        dist.sort()
        
        result = 0
        currentTime = 0
        for distance in dist:
            if currentTime >= distance:
                break
            result += 1
            currentTime += 1
        return result