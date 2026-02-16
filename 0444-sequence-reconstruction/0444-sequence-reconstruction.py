from collections import defaultdict, deque

class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for sequence in sequences:
            for i in range(1, len(sequence)):
                nodeU, nodeV = sequence[i - 1], sequence[i]
                graph[nodeU].append(nodeV)
                indegree[nodeV] += 1
        queue = deque()
        for node in range(1, n + 1):
            if indegree[node] == 0:
                queue.append(node)
        index = 0
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            if nums[index] != node:
                return False
            index += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if index < n:
            return False
        return True