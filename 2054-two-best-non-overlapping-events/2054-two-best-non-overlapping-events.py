import heapq
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda event: event[0]) # sort by start time
        minHeap = [] # contains pair of event end time and value of the event
        result = 0
        maxValue = 0
        for start, end, currentValue in events:
            while minHeap and minHeap[0][0] < start:
                _, value = heapq.heappop(minHeap)
                maxValue = max(maxValue, value)
            result = max(result, maxValue + currentValue)
            heapq.heappush(minHeap, [end, currentValue])
        return result