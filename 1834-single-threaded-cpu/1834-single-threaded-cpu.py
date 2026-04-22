import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # time: O(N log N)
        # space: O(N)
        # method: sort + min heap

        n = len(tasks)
        jobs = []
        for i in range(n):
            jobs.append([tasks[i][0], tasks[i][1], i])
        jobs.sort()
        
        currentTime = 0
        index = 0
        result = []
        availableForRun = []

        while index < n:
            while index < n and jobs[index][0] <= currentTime:
                heapq.heappush(availableForRun, (jobs[index][1], jobs[index][2]))
                index += 1
            if availableForRun:
                processTime, jobId = heapq.heappop(availableForRun)
                result.append(jobId)
                currentTime += processTime
            else:
                currentTime = jobs[index][0]
        while availableForRun:
            _, jobId = heapq.heappop(availableForRun)
            result.append(jobId)
        return result
