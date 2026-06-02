from sortedcontainers import SortedList

class SegmentTree:
    def __init__(self, length: int) -> None:
        self.st = [0] * length * 4
        self.n = length
    
    def update(self, position: int, value: int) -> None:
        self.__update(1, 0, self.n - 1, position, value)
    
    def __update(self, pointer: int, left: int, right: int, position: int, value: int) -> None:
        if left > right or left > position or right < position:
            return
        if left == position == right:
            self.st[pointer] = value
            return
        self.__update(2 * pointer, left, (left + right) // 2, position, value) # left child
        self.__update(2 * pointer + 1, (left + right) // 2 + 1, right, position, value) # right child
        self.st[pointer] = max(self.st[2 * pointer], self.st[2 * pointer + 1])
    
    def get_max(self, right: int) -> int:
        return self.__query(1, 0, self.n - 1, 0, right)
    
    def __query(self, pointer: int, left: int, right: int, query_left: int, query_right: int) -> int:
        if left > right or left > query_right or right < query_left:
            return 0
        if left >= query_left and right <= query_right:
            return self.st[pointer]
        left_value = self.__query(2 * pointer, left, (left + right) // 2, query_left, query_right) # left child
        right_value = self.__query(2 * pointer + 1, (left + right) // 2 + 1, right ,query_left, query_right) # right child
        value = max(left_value, right_value)
        return value

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # time: O(N log N) N is the query size
        # space: O(N)
        # method: segment tree
        n = len(queries)
        obstacles = [0]
        for i in range(n):
            query_type = queries[i][0]
            if query_type == 1:
                x = queries[i][1]
                obstacles.append(x)
        
        obstacles.sort()
        obstacle_position = {}
        length = len(obstacles)
        for i in range(length):
            x = obstacles[i]
            obstacle_position[x] = i
        
        current_obstacles = SortedList([0])
        segment_tree = SegmentTree(length)
        
        result = []
        for i in range(n):
            if queries[i][0] == 1: # obstacle
                x = queries[i][1]
                index = current_obstacles.bisect_left(x) - 1
                value = x - current_obstacles[index]
                position = obstacle_position[x]
                segment_tree.update(position, value)
                index = current_obstacles.bisect_right(x)
                if index < len(current_obstacles):
                    value = current_obstacles[index] - x
                    position = obstacle_position[current_obstacles[index]]
                    segment_tree.update(position, value)
                current_obstacles.add(x)
            else: # query
                x = queries[i][1]
                sz = queries[i][2]
                index = current_obstacles.bisect_left(x) - 1
                value = x - current_obstacles[index]
                if value >= sz:
                    result.append(True)
                    continue
                x = current_obstacles[index]
                position = obstacle_position[x]
                value = segment_tree.get_max(position)
                result.append(value >= sz)
        
        return result