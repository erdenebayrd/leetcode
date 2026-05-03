from sortedcontainers import SortedList

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # time: O(N log N)
        # space: O(N)
        # method: greedy
        
        n = len(nums)
        groups = n // k
        if groups * k != n:
            return False

        sl = SortedList(nums)

        def checkAndRemove(startNumber: int) -> bool:
            for i in range(k):
                number = startNumber + i
                if number not in sl:
                    return False
                sl.remove(number)
            return True
        
        for _ in range(groups):
            startNumber = sl[0]
            if checkAndRemove(startNumber) is False:
                return False
        return True