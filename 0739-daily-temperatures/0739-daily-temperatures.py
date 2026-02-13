import heapq

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # time: O(N * Log N)
        # space: O(N)
        minHeapWithIndex = []
        n = len(temperatures)
        result = [0] * n
        for index in range(n):
            
            while minHeapWithIndex and minHeapWithIndex[0][0] < temperatures[index]:
                _, previousIndex = heapq.heappop(minHeapWithIndex)
                result[previousIndex] = index - previousIndex
            
            heapq.heappush(minHeapWithIndex, [temperatures[index], index])
        
        return result