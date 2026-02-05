from collections import defaultdict

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # time: O(N * Log N)
        # space: O(N + M)
        fullBlooms = defaultdict(int)
        for start, end in flowers:
            fullBlooms[start] += 1
            fullBlooms[end + 1] -= 1
        for arrive in people:
            if arrive not in fullBlooms:
                fullBlooms[arrive] = 0
        fullBlooms = sorted([[timestamp, flowers] for timestamp, flowers in fullBlooms.items()])
        for i in range(1, len(fullBlooms)):
            fullBlooms[i][1] += fullBlooms[i - 1][1]
        
        fullBloomsByTime = defaultdict(int)
        for timestamp, flowers in fullBlooms:
            fullBloomsByTime[timestamp] = flowers
        answer = []
        for arrive in people:
            answer.append(fullBloomsByTime[arrive])
        return answer