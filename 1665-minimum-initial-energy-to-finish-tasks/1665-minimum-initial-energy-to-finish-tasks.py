class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # time: O(N log N)
        # space: O(N)
        # method: observation

        diff = []
        for actual, minimum in tasks:
            diff.append(minimum - actual)
        
        tasks = sorted(zip(tasks, diff), key=lambda x: x[1], reverse=True)
        # print(tasks)
        
        result = 0
        current = 0
        for [actual, minimum], _ in tasks:
            if current < minimum:
                diff = minimum - current
                current = minimum
                result += diff
            current -= actual
        return result