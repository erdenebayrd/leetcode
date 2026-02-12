import bisect

class SnapshotArray:

    def __init__(self, length: int): # O(N)
        self.snapId = 0
        self.array = [[[self.snapId, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None: # O(1)
        snapId, value = self.array[index][-1]
        if snapId == self.snapId:
            value = val
            self.array[index][-1] = [snapId, value]
        else: # snapId != self.snapid (updated)
            self.array[index].append([self.snapId, val])

    def snap(self) -> int: # O(1)
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int: # O(Log N) N is the number of snap() called
        # print(self.array)
        snapshots = self.array[index] # contains [version, value], [version, value] etc
        # print(snapshots)
        snapshotIndex = bisect.bisect_left(snapshots, [snap_id, -1])
        if snapshotIndex >= len(snapshots) or snapshots[snapshotIndex][0] != snap_id:
            snapshotIndex -= 1
        # low, high = -1, len(snapshots)
        # while low + 1 < high:
        #     middle = (low + high) // 2
        #     version = snapshots[middle][0]
        #     if snap_id >= version:
        #         low = middle
        #     else: # snap_id < version
        #         high = middle

        # snapshotIndex = low
        return snapshots[snapshotIndex][-1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id) 