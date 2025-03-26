class StockPrice:

    def __init__(self):
        self.timeStampsSl = SortedList([])
        self.pricesDict = {}
        self.pricesSl = SortedList([])

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timeStampsSl:
            self.timeStampsSl.remove(timestamp)
            self.pricesSl.remove(self.pricesDict[timestamp])
        self.timeStampsSl.add(timestamp)
        self.pricesDict[timestamp] = price
        self.pricesSl.add(price)

    def current(self) -> int:
        return self.pricesDict[self.timeStampsSl[-1]]

    def maximum(self) -> int:
        return self.pricesSl[-1]

    def minimum(self) -> int:
        return self.pricesSl[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()