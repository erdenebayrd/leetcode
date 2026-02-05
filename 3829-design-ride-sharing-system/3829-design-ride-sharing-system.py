from collections import deque

class RideSharingSystem:

    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.currentRiders = set() # hash map for currentRiders
        self.cancelledRiders = set() # lazy deletion from riders

    def addRider(self, riderId: int) -> None: # O(1)
        self.riders.append(riderId)
        self.currentRiders.add(riderId)

    def addDriver(self, driverId: int) -> None: # O(1)
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.riders and self.riders[0] in self.cancelledRiders:
            cancelledRider = self.riders.popleft()
            self.cancelledRiders.discard(cancelledRider)
        if self.riders and self.drivers:
            rider = self.riders.popleft()
            driver = self.drivers.popleft()
            self.currentRiders.discard(rider)
            return [driver, rider]
        return [-1, -1]


    def cancelRider(self, riderId: int) -> None:
        if riderId not in self.currentRiders:
            return
        self.cancelledRiders.add(riderId)
        self.currentRiders.discard(riderId)



# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)