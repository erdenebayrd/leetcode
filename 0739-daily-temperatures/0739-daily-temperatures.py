from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # time: O(N)
        # space: O(N)
        n = len(temperatures)
        result = [0] * n
        monotonicDecreasing = deque() # contains indexes of temperatures which is "day"
        for index in range(n): # day
            while monotonicDecreasing and temperatures[monotonicDecreasing[-1]] < temperatures[index]:
                previousIndex = monotonicDecreasing.pop()
                result[previousIndex] = index - previousIndex # how many days needed to be waited from day "previousIndex"
            monotonicDecreasing.append(index)
        
        del monotonicDecreasing
        return result