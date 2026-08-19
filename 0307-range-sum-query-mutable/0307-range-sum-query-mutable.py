class FenwickTree:
    def __init__(self, nums: list) -> None:
        self.size = len(nums)
        self.ft = [0] * (self.size + 1)
        for i in range(self.size):
            self.add(i + 1, nums[i])
    
    def add(self, position: int, value: int) -> None:
        while position <= self.size:
            self.ft[position] += value
            position += position & -position
    
    def query(self, left: int, right: int) -> int:
        return self.__query(right) - self.__query(left - 1)
    
    def __query(self, right: int) -> int:
        result = 0
        while right > 0:
            result += self.ft[right]
            right -= right & -right
        return result

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ft = FenwickTree(nums)

    def update(self, index: int, val: int) -> None:
        self.ft.add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.ft.query(left + 1, right + 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)