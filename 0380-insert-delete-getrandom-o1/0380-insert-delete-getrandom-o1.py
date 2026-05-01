from random import randint

class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.set = {}

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        
        self.set[val] = len(self.arr)
        self.arr.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        
        index = self.set[val]
        if index == len(self.arr) - 1:
            self.arr.pop()
            del self.set[val]
        else:
            lastIndex = len(self.arr) - 1
            lastVal = self.arr[lastIndex]
            self.arr[index], self.arr[lastIndex] = self.arr[lastIndex], self.arr[index]
            del self.set[val]
            self.set[lastVal] = index
            self.arr.pop()

        return True

    def getRandom(self) -> int:
        index = randint(0, len(self.arr) - 1)
        return self.arr[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()