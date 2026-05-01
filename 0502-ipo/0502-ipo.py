import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # time O(n log n + k log n) -> O((n + k) * log n)
        # space: O(n)
        # method: 2 heaps
        n = len(capital)
        ready = [] # ready to start projects heap by total profit (max at top)
        others = [] # other projects not available for w capital right now, heap by k (min at top)
        for i in range(n):
            if capital[i] <= w:
                ready.append(-profits[i]) # it's max heap
            else:
                others.append((capital[i], profits[i]))
        heapq.heapify(ready)
        heapq.heapify(others)
        
        while k and ready:
            k -= 1
            profit = -heapq.heappop(ready)
            w += profit
            while others and w >= others[0][0]:
                _, profit = heapq.heappop(others)
                heapq.heappush(ready, -profit)
        return w