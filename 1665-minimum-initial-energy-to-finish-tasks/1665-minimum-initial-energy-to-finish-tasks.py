class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # time: O(N log N)
        # space: O(N)
        # method: observation
        
        tasks = sorted(tasks, key=lambda x: x[1] - x[0], reverse=True)
        # print(tasks)
        
        result = 0
        current = 0
        for actual, minimum in tasks:
            if current < minimum:
                diff = minimum - current
                current = minimum
                result += diff
            current -= actual
        return result