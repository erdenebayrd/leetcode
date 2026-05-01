class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # time: O(N log N)
        # space: O(1)
        # method: binary search
        n = len(dist)
        low, high = 0, max(dist) * 100 + 1

        def can(speed: int) -> bool:
            total = 0
            for i in range(n):
                spend = (dist[i] // speed) + int(dist[i] % speed > 0)
                if i == n - 1:
                    total += dist[i] / speed
                else:
                    total += spend
            # print(total, hour)
            return total <= hour

        while low + 1 < high:
            mid = (low + high) // 2
            if can(mid):
                high = mid
            else:
                low = mid
        if high == max(dist) * 100 + 1:
            high = -1
        # print(can(high))
        return high