class ProductOfNumbers:

    def __init__(self):
        self.prefix = []
        self.last_zero_index = -1

    def add(self, num: int) -> None:
        prev_number = 1
        if self.prefix and self.prefix[-1] != 0:
            prev_number = self.prefix[-1]
        if num == 0:
            self.last_zero_index = len(self.prefix)
        self.prefix.append(prev_number * num)

    def getProduct(self, k: int) -> int:
        left = len(self.prefix) - k
        if left <= self.last_zero_index:
            return 0
        
        if left == 0 or self.prefix[left - 1] == 0:
            return self.prefix[-1]
        
        return self.prefix[-1] // self.prefix[left - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)