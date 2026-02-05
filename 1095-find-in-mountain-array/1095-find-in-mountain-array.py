# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        low, high = -1, mountainArr.length() - 1
        while low + 1 < high:
            mid = (low + high) // 2
            # print("-" * 100)
            # print(mid, mid + 1)
            # print(mountainArr.get(mid), mountainArr.get(mid + 1))
            # print("-" * 100)
            if mountainArr.get(mid) < mountainArr.get(mid + 1): # increasing
                low = mid + 1
            else:
                high = mid
        peakIndex = high
        low, high = -1, peakIndex + 1
        while low + 1 < high:
            mid = (low + high) // 2
            value = mountainArr.get(mid)
            if target < value:
                high = mid
            elif target > value:
                low = mid
            else: # we found a target at index "mid"
                return mid
        
        low, high = peakIndex - 1, mountainArr.length()
        while low + 1 < high:
            mid = (low + high) // 2
            value = mountainArr.get(mid)
            if target < value:
                low = mid
            elif target > value:
                high = mid
            else:
                return mid
        return -1