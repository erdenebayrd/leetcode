class LRUCache:

    def __init__(self, capacity: int):
        self.N = int(2e5 + 1)
        self.ft = [0] * self.N
        self.pos = {}
        self.curPos = 1
        self.capacity = capacity
        self.val = {}

    def add(self, pos: int, val: int) -> None:
        while pos < self.N:
            self.ft[pos] += val
            pos += (-pos & pos)

    def getSum(self, pos: int) -> int:
        res = 0
        while pos > 0:
            res += self.ft[pos]
            pos -= (-pos & pos)
        return res
    
    def getRange(self, l: int, r: int) -> int:
        return self.getSum(r) - self.getSum(l - 1)

    def get(self, key: int) -> int:
        if key not in self.pos:
            return -1
        x = self.getRange(self.pos[key], self.curPos)
        if x <= self.capacity:
            self.add(self.pos[key], -1)
            self.pos[key] = self.curPos
            self.add(self.curPos, 1)
            self.curPos += 1
            return self.val[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        self.val[key] = value
        if key in self.pos:
            self.add(self.pos[key], -1)
        self.pos[key] = self.curPos
        self.add(self.curPos, 1)
        self.curPos += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)