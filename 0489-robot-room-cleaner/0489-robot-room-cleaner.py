# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        """
            we can use DFS recursive function like visiting every node in a graph by calling API's
        """
        # time: O(rows * cols - area_of_obstacles)
        # space: O(rows * cols - area_of_obstacles)
        # method: DFS

        cleaned = set()
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def dfs(row: int, col: int, current_direction: int) -> None:
            cleaned.add((row, col))
            robot.clean()
            for index in range(len(directions)):
                new_direction = (current_direction + index) % len(directions)
                delta_row, delta_col = directions[new_direction]
                next_row, next_col = row + delta_row, col + delta_col
                if (next_row, next_col) not in cleaned and robot.move() is True:
                    dfs(next_row, next_col, new_direction)
                    # need to go back with same direction
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnLeft()
        
        dfs(0, 0, 0)