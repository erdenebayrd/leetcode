class TwoSum:

    def __init__(self):
        self.sl = SortedList([])
        self.cnt = defaultdict(int)

    def add(self, number: int) -> None:
        self.sl.add(number)
        self.cnt[number] += 1

    def find(self, value: int) -> bool:
        if value % 2 == 0 and (value//2) in self.cnt and self.cnt[value//2] > 1:
            return True
        for key in self.cnt:
            if value != 2 * key and value - key in self.sl:
                # print(value, key, value - key, self.sl)
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)