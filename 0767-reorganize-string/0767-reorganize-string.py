import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = []
        for ch in count:
            max_heap.append((-count[ch], ch))
        heapq.heapify(max_heap)

        result = []
        while max_heap:
            first_freq, first_ch = heapq.heappop(max_heap)
            if result and result[-1] == first_ch:
                return ""
            result.append(first_ch)
            first_freq += 1
            if max_heap:
                second_freq, second_ch = heapq.heappop(max_heap)
                result.append(second_ch)
                second_freq += 1
                if second_freq < 0:
                    heapq.heappush(max_heap, (second_freq, second_ch))
            if first_freq < 0:
                heapq.heappush(max_heap, (first_freq, first_ch))
        return "".join(result)