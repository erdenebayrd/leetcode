class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = defaultdict(lambda: defaultdict(bool))
        for x, y in obstacles:
            obs[x][y] = True
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        currentDirIndex = 3
        currentX, currentY = 0, 0
        result = 0
        for command in commands:
            if command == -1: # right
                currentDirIndex = (currentDirIndex + 1) % len(dirs)
            elif command == -2: # left
                currentDirIndex = (currentDirIndex - 1) % len(dirs)
            else:
                while command > 0:
                    nextX, nextY = dirs[currentDirIndex][0] + currentX, dirs[currentDirIndex][1] + currentY
                    if obs[nextX][nextY] is False:
                        currentX, currentY = nextX, nextY
                        result = max(result, currentX ** 2 + currentY ** 2)
                    else:
                        break
                    command -= 1
                # print(currentDirIndex, currentX, currentY)
        return result