class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        startAt = [0] * n
        cnt = [0] * n
        for st, ed in meetings:
            room = n
            startAtMin, roomMin = int(5e10 + 1), n
            for i in range(n):
                if startAt[i] <= st:
                    room = min(room, i)
                if startAtMin > startAt[i]:
                    startAtMin = startAt[i]
                    roomMin = i
            if room == n:
                room = roomMin
            print(startAtMin, room)
            start = max(startAt[room], st)
            end = start + ed - st
            startAt[room] = end
            cnt[room] += 1
        room, usage = -1, -1
        for i in range(n):
            if usage < cnt[i]:
                usage = cnt[i]
                room = i
        return room