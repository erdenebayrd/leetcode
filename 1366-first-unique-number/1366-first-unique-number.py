class FirstUnique:

    def __init__(self, nums: List[int]):
        self.uniqueQueue = OrderedDict()
        self.isUnique = {}
        for x in nums:
            if x not in self.isUnique:
                self.isUnique[x] = True
            else:
                self.isUnique[x] = False
        for x in nums:
            if self.isUnique[x] is True:
                self.uniqueQueue[x] = ""

    def showFirstUnique(self) -> int:
        if len(self.uniqueQueue) > 0:
            return next(iter(self.uniqueQueue))
        return -1

    def add(self, value: int) -> None:
        if value not in self.isUnique:
            self.isUnique[value] = True
            self.uniqueQueue[value] = ""
        else:
            self.isUnique[value] = False
            if value in self.uniqueQueue:
                self.uniqueQueue.pop(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)