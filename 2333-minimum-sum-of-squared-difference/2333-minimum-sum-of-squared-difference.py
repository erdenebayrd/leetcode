class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # time: O(N + M + log N)
        # space: O(N)
        # method: bucket sort + binary search
        """
            nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
            diff = 3, 3, 4, 3 
            squared = 9, 9, 16, 9
            sum = 43
        """
        n = len(nums1)

        def bucket_sort(values: list) -> list:
            count = [0] * (max(values) + 1)
            for value in values:
                count[value] += 1
            result = []
            for value in range(min(values), max(values) + 1):
                if count[value] == 0:
                    continue
                result.extend([value] * count[value])
            return result


        diff = bucket_sort([abs(nums1[i] - nums2[i]) for i in range(n)])
        prefix = diff[:]
        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        def get_sum(left: int, right: int) -> int:
            if left == 0:
                return prefix[right]
            return prefix[right] - prefix[left - 1]

        k = k1 + k2
        low, high = -1, n
        while low + 1 < high:
            mid = (low + high) // 2
            if get_sum(mid, n - 1) - diff[mid] * (n - mid) <= k:
                high = mid
            else:
                low = mid
        
        for i in range(high, n):
            k -= (diff[i] - diff[high])
            diff[i] = diff[high]
        
        assert k >= 0
        if k > 0:
            value = k // (n - high)
            for i in range(high, n):
                diff[i] = max(0, diff[i] - value)
            k -= value * (n - high)
            for i in range(n - 1, n - 1 - k, -1):
                diff[i] = max(0, diff[i] - 1)
        
        result = 0
        for value in diff:
            result += value * value
        return result