from random import randint
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.positions = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.positions[val].add(len(self.arr))
        self.arr.append(val)
        return len(self.positions[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False
        lastIndex = len(self.arr) - 1
        lastValue = self.arr[lastIndex]
        index = next(iter(self.positions[val]))
        if lastValue == val:
            self.positions[val].remove(lastIndex)
            if len(self.positions[val]) == 0:
                del self.positions[val]
            self.arr.pop()
        else: # values are different
            self.arr[index] = lastValue
            self.arr.pop()
            self.positions[val].remove(index)
            if len(self.positions[val]) == 0:
                del self.positions[val]
            self.positions[lastValue].remove(lastIndex)
            self.positions[lastValue].add(index)

        return True

    def getRandom(self) -> int:
        index = randint(0, len(self.arr) - 1)
        return self.arr[index]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()