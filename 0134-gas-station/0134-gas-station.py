import heapq

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]
        prefix = diff + diff
        for i in range(1, 2 * n):
            prefix[i] += prefix[i - 1]
        
        remove = {}
        min_heap = prefix[:n]
        heapq.heapify(min_heap)
        current = 0
        for i in range(n):
            while min_heap and min_heap[0] in remove:
                value = heapq.heappop(min_heap)
                remove[value] -= 1
                if remove[value] == 0:
                    del remove[value]
            if current <= min_heap[0]:
                return i
            
            if prefix[i] not in remove:
                remove[prefix[i]] = 0
            remove[prefix[i]] += 1
            current = prefix[i]
            heapq.heappush(min_heap, prefix[i + n])
        return -1