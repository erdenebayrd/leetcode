class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # time: O(N * 2 ^ N) multiplied by N due to sort
        # space: O(2 ^ N)
        # method: meet in the middle
        n = len(stones)
        total = sum(stones)
        
        def getSubset(arr: List[int]) -> List[int]: # O(2 ^ len(arr))
            n = len(arr)
            subset = [0] * (1 << n)
            for bitmask in range(1, 1 << n):
                lastBit = -bitmask & bitmask
                index = lastBit.bit_length() - 1
                subset[bitmask] = subset[bitmask ^ lastBit] + arr[index]
            return subset
        
        left = getSubset(stones[:n // 2])
        right = getSubset(stones[n // 2:])
        right.sort()

        def closest(arr: List[int], target: int) -> int: # O(N) from O(log (2 ^ N))
            index = bisect.bisect_left(arr, target)
            if index == len(arr):
                return arr[-1]
            if index == 0:
                return arr[0]
            if abs(arr[index] - target) < abs(arr[index - 1] - target):
                return arr[index]
            return arr[index - 1]
        
        result = float("inf")
        for number in left:
            target = total / 2 - number
            first = number + closest(right, target)
            second = total - first
            result = min(result, abs(first - second))
        return result