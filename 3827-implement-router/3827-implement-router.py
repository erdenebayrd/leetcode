class Router:

    def __init__(self, memoryLimit: int):
        self.seen = set()
        self.limit = memoryLimit
        self.queue = deque()
        self.sl = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.seen:
            return False
        if len(self.queue) >= self.limit:
            self.forwardPacket()
        # add
        self.queue.append([source, destination, timestamp])
        self.seen.add((source, destination, timestamp))
        if destination not in self.sl:
            self.sl[destination] = SortedList([])
        self.sl[destination].add(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.queue) == 0:
            return []
        [src, dest, timestamp] = self.queue.popleft()
        self.seen.remove((src, dest, timestamp))
        self.sl[dest].remove(timestamp)
        return [src, dest, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.sl:
            return 0
        ri = self.sl[destination].bisect_right(endTime)
        le = self.sl[destination].bisect_left(startTime)
        return ri - le


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)