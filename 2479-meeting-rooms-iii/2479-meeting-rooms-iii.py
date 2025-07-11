class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        endTimes = [0] * n
        cntRooms = [0] * n
        meetings.sort()
        for st, ed in meetings:
            mnIdx = -1
            mnVal = int(1e18)
            found = False
            for i in range(n):
                if mnVal > endTimes[i]:
                    mnVal = endTimes[i]
                    mnIdx = i
                if endTimes[i] <= st:
                    cntRooms[i] += 1
                    endTimes[i] = ed
                    found = True
                    break
            if found is False:
                endTimes[mnIdx] += (ed - st)
                cntRooms[mnIdx] += 1
        mxIdx, mxVal = -1, -1
        for i in range(n):
            if mxVal < cntRooms[i]:
                mxVal = cntRooms[i]
                mxIdx = i
        return mxIdx