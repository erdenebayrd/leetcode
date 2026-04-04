class StockSpanner:
    # time: O(N)
    # space: O(N)
    # method: monotonic stack (prev strictly greater element)

    def __init__(self):
        self.stock = []
        self.stack = []

    def next(self, price: int) -> int:
        while self.stack and self.stock[self.stack[-1]] <= price:
            self.stack.pop()
        prevGreater = -1
        if self.stack:
            prevGreater = self.stack[-1]
        self.stack.append(len(self.stock))
        self.stock.append(price)
        return len(self.stock) - prevGreater - 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)