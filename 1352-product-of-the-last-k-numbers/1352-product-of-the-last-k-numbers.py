class ProductOfNumbers:

    def __init__(self): # O(1)
        self.prefix = []

    def add(self, num: int) -> None: # O(1)
        if num == 0:
            self.prefix = []
            return
        
        prev_number = 1
        if self.prefix:
            prev_number = self.prefix[-1]
        self.prefix.append(num * prev_number)

    def getProduct(self, k: int) -> int: # O(1)
        left = len(self.prefix) - k
        if left < 0:
            return 0
        if left == 0:
            return self.prefix[-1]
        return self.prefix[-1] // self.prefix[left - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)