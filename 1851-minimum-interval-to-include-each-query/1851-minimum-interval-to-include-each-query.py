class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        # time: O((n log n + m log m) n is len of intervals, m is len of queries
        # space: O(n + m)
        # method: min heap + sorting
        
        n = len(intervals)
        intervals.sort()
        
        m = len(queries)
        queries_sorted = []
        for i in range(m):
            queries_sorted.append((queries[i], i))
        
        result = [-1] * m
        queries_sorted.sort()
        
        min_heap = [] # interval length, interval right value

        right = 0
        for query_point, query_index in queries_sorted:
            while right < n and intervals[right][0] <= query_point:
                interval_left, interval_right = intervals[right]
                interval_length = interval_right - interval_left + 1
                heapq.heappush(min_heap, (interval_length, interval_right))
                right += 1
            
            while min_heap and min_heap[0][1] < query_point:
                heapq.heappop(min_heap)
            
            if min_heap:
                result[query_index] = min_heap[0][0]
        return result