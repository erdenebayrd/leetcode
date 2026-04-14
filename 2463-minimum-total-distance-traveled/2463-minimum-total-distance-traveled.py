class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # time: O(N ^ 3)
        # space: O(N ^ 2)
        # method: DP
        robot.sort()
        factory.sort()
        
        n = len(factory)
        m = len(robot)
        
        def calculateCost(factoryIndex: int, robotIndex: int) -> int:
            if robotIndex >= m:
                return 0
            positionFactory, _ = factory[factoryIndex]
            positionRobot = robot[robotIndex]
            return abs(positionRobot - positionFactory)

        @cache
        def solve(factoryIndex: int, robotIndex: int) -> float:
            if robotIndex >= m:
                return 0
            if factoryIndex >= n:
                return float('inf')
            cost = 0
            result = solve(factoryIndex + 1, robotIndex)
            _, limit = factory[factoryIndex]
            for robots in range(1, limit + 1):
                cost += calculateCost(factoryIndex, robotIndex + robots - 1)
                result = min(result, cost + solve(factoryIndex + 1, robotIndex + robots))
            return result
        
        result = solve(0, 0)
        return result