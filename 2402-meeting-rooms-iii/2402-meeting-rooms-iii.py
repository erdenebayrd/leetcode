class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        cnt = [0] * n
        available = list(range(n)) # rooms
        busy = [] # first value would be end time, second be room number
        heapq.heapify(available)
        heapq.heapify(busy)
        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                endTime, room = heapq.heappop(busy)
                heapq.heappush(busy, (endTime + (end - start), room))
            cnt[room] += 1
        return cnt.index(max(cnt))