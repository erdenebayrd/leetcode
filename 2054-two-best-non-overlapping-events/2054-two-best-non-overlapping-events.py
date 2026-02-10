import heapq
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # time: O(N * Log N)
        # space: O(N) # minHeap can store all the events at the same time when all events intersected each other somehow
        # method: priority queue/min heap

        # n = len(events)
        # events.sort(key=lambda event: event[0]) # sort by start time
        # minHeap = [] # contains pair of event end time and value of the event
        # result = 0
        # maxValue = 0
        # for start, end, currentValue in events:
        #     while minHeap and minHeap[0][0] < start:
        #         _, value = heapq.heappop(minHeap)
        #         maxValue = max(maxValue, value)
        #     result = max(result, maxValue + currentValue)
        #     heapq.heappush(minHeap, [end, currentValue])
        # return result
        # ---------------------------------------------------------------------------------------------------------------
        # time: O(N * log N) # sorting
        # space: O(N) storing events in 1D array with start and endtime with it's values
        # method: greedy
        times = []
        for start, end, value in events:
            times.append([start, True, value]) # True means starts at this time
            times.append([end + 1, False, value]) # False means end at here, why "end + 1" not "end". The reason is we can start from end + 1, can't start from end because end time is inclusive so that we can't directly start at endtime
        times.sort()
        # print(times)
        previousMaxValue = 0
        result = 0
        for time, isStart, value in times:
            if isStart is True: # starting at "time"
                result = max(result, value + previousMaxValue)
            else: # end at "time", we can start from "time"
                previousMaxValue = max(previousMaxValue, value)
        return result