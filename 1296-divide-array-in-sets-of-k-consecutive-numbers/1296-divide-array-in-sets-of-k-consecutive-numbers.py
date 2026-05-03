import heapq
from collections import defaultdict

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # time: O(N log N)
        # space: O(N)
        # method: greedy
        
        n = len(nums)
        groups = n // k
        if groups * k != n:
            return False

        minHeap = []
        count = defaultdict(int)
        for i in range(n):
            count[nums[i]] += 1
            heapq.heappush(minHeap, nums[i])
        
        while minHeap:
            top = heapq.heappop(minHeap)
            if top not in count:
                continue
            for i in range(k): # one group eliminated from count dictionary
                number = top + i
                if number not in count:
                    return False
                count[number] -= 1
                if count[number] == 0:
                    del count[number]

        return True