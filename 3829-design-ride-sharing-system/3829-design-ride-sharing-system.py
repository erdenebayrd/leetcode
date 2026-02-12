from collections import deque

class RideSharingSystem:
    def __init__(self):
        self.drivers = deque()
        self.riders = deque()
        self.currentActiveRiders = set()
        self.lazyDeletedRiders = set()
        

    def addRider(self, riderId: int) -> None: # O(1)
        self.riders.append(riderId)
        self.currentActiveRiders.add(riderId)

    def addDriver(self, driverId: int) -> None: # O(1)
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]: # O(N) amortized, overall O(N) for all calls
        while self.riders and self.riders[0] in self.lazyDeletedRiders:
            riderId = self.riders.popleft()
            self.lazyDeletedRiders.discard(riderId)
        if not self.riders or not self.drivers:
            return [-1, -1]
        riderId = self.riders.popleft()
        driverId = self.drivers.popleft()
        return [driverId, riderId]

    def cancelRider(self, riderId: int) -> None: # O(1)
        if riderId not in self.currentActiveRiders:
            return
        self.lazyDeletedRiders.add(riderId)
        self.currentActiveRiders.discard(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)