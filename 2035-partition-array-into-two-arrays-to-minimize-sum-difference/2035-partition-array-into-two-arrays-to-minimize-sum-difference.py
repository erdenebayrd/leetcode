class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # time: O(n * (2 ^ n))
        # space: O(2 ^ n)
        # method: meet in the middle
        n = len(nums) // 2
        nums1 = nums[:n]
        nums2 = nums[n:]
        total = sum(nums)

        def getSubsetSumByBitCount(arr: List[int]) -> dict:
            n = len(arr)
            subsetSum = [0] * (1 << n)
            for bitmask in range(1, 1 << n):
                lowestBit = -bitmask & bitmask
                index = lowestBit.bit_length() - 1 # O(1) getting highest 1 position
                subsetSum[bitmask] = subsetSum[bitmask ^ lowestBit] + arr[index]
            result = defaultdict(list)
            for bitmask in range(1 << n):
                bits = bitmask.bit_count()
                result[bits].append(subsetSum[bitmask])
            for bits in result:
                result[bits].sort()
            return result
        
        def closestNumber(arr: List[int], target: int) -> int:
            index = bisect.bisect_left(arr, target)
            if index == len(arr):
                return arr[-1]
            if index == 0:
                return arr[0]
            if abs(arr[index] - target) < abs(arr[index - 1] - target):
                return arr[index]
            return arr[index - 1]

        left = getSubsetSumByBitCount(nums1)
        right = getSubsetSumByBitCount(nums2)
        result = float('inf')
        for bits in left:
            neededBits = n - bits
            for leftNumber in left[bits]:
                neededNumber = total / 2 - leftNumber
                rightNumber = closestNumber(right[neededBits], neededNumber)
                first = leftNumber + rightNumber
                second = total - first
                result = min(result, abs(first - second))
        return result