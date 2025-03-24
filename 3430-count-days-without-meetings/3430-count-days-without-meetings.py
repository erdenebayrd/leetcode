class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # time: O(N * Log N)
        # space: O(1)
        totalMeetingTime = 0
        meetings.sort()
        curStart, curEnd = meetings[0]
        for i in range(1, len(meetings)):
            start, end = meetings[i]
            if start <= curEnd: # overlap
                curEnd = max(curEnd, end)
            else:
                totalMeetingTime += curEnd - curStart + 1
                curStart = start
                curEnd = end
        totalMeetingTime += curEnd - curStart + 1
        return days - totalMeetingTime