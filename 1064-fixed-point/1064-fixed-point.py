class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        # time: O(log N)
        # space: O(1)
        # method: binary search
        """
            since the given array is sorted and contains distinct integers
            we can use binary search by comparing value with it's index
            then decide which side we need to go
        """
        n = len(arr)
        low, high = -1, n
        while low + 1 < high:
            mid = (low + high) // 2
            if mid <= arr[mid]:
                high = mid
            else:
                low = mid
        if high == n or high < arr[high]:
            high = -1
        return high