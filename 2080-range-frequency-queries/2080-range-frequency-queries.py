import bisect

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.indices = {}
        for i in range(len(arr)):
            if arr[i] not in self.indices:
                self.indices[arr[i]] = []
            self.indices[arr[i]].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.indices:
            return 0
        right = bisect.bisect_right(self.indices[value], right)
        left = bisect.bisect_left(self.indices[value], left)
        return right - left


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)