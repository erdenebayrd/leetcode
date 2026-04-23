from sortedcontainers import SortedList

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        # time: O(Q log Q + log N (Q + N))
        # space: O(Q)

        def findClosest(roomIds, preferred: int) -> int:
            if not roomIds:
                return -1
            index = roomIds.bisect_left(preferred)
            if index == len(roomIds):
                return roomIds[-1]
            if index == 0:
                return roomIds[0]
            if abs(roomIds[index] - preferred) < abs(roomIds[index - 1] - preferred):
                return roomIds[index]
            return roomIds[index - 1]

        query = []
        m = len(queries)
        for i in range(m):
            preferred, minSize = queries[i]
            query.append([minSize, preferred, i])
        query.sort()
        result = [-1] * m
        rooms.sort(key=lambda x: x[1])
        n = len(rooms)
        currentRoomIndex = n - 1
        roomIds = SortedList()
        for i in range(m - 1, -1, -1):
            minSize, preferred, index = query[i]
            while currentRoomIndex >= 0 and minSize <= rooms[currentRoomIndex][1]:
                roomIds.add(rooms[currentRoomIndex][0])
                currentRoomIndex -= 1
            closestRoomId = findClosest(roomIds, preferred)
            result[index] = closestRoomId
        return result