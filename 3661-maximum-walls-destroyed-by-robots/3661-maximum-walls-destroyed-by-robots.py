import bisect

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # time: O(N log N)
        # space: O(N)
        # method: DP
        sortedRobots = sorted(zip(robots, distance))
        n = len(robots)
        for i in range(n):
            position, dist = sortedRobots[i]
            robots[i] = position
            distance[i] = dist

        walls.sort()
        
        def countWalls(left: int, right: int) -> int:
            return bisect.bisect_right(walls, right) - bisect.bisect_left(walls, left)

        def shoot(index: int, direction: str) -> int: # index of robot, direction is left or right
            left, right = -1, -1
            if direction == "left":
                left = robots[index] - distance[index]
                if index > 0:
                    left = max(left, robots[index - 1] + 1)
                right = robots[index]
            else: # right
                left = robots[index]
                right = robots[index] + distance[index]
                if index + 1 < n:
                    right = min(right, robots[index + 1] - 1)
            return countWalls(left, right)

        def countWallsCurrentLeftPrevRight(index: int) -> int: # index of robot shoot left when prev robot already fired right:
            total = countWalls(robots[index - 1], robots[index])
            total = min(total, shoot(index - 1, "right") + shoot(index, "left"))
            return total - shoot(index - 1, "right")

        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = shoot(0, "left")
        dp[0][1] = shoot(0, "right")
        for i in range(1, n):
            # if i'th robot fire LEFT
                # i - 1 also fired LEFT
            dp[i][0] = dp[i - 1][0] + shoot(i, "left")
                # i - 1 fired RIGHT
            dp[i][0] = max(dp[i][0], dp[i - 1][1] + countWallsCurrentLeftPrevRight(i))

            # If i'th robot fire RIGHT
                # i - 1 robot shoot LEFT
            dp[i][1] = dp[i - 1][0] + shoot(i, "right")
            dp[i][1] = max(dp[i][1], dp[i - 1][1] + shoot(i, "right"))
        
        # for i in range(n):
        #     print(dp[i])

        return max(dp[n - 1][0], dp[n - 1][1])