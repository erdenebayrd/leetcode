class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        # time: O(n * sqrt(n) + n * log(n))
        # space: O(n * log n)
        # method: rmq + number theory

        n = len(nums)
        dividers = []
        for i in range(1, n + 1):
            if n % i == 0:
                dividers.append(i)
        
        diff = [0] * n
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                diff[i] = 1
            diff[i] += diff[i - 1]
        
        # print(dividers)
        # print(diff)

        # sparse table for max & min values by O(n * log n)
        m = n.bit_length()
        max_values = [[float('-inf')] * m for _ in range(n)]
        min_values = [[float('inf')] * m for _ in range(n)]
        for i in range(n):
            max_values[i][0] = nums[i]
            min_values[i][0] = nums[i]
        
        # TODO: build sparse table
        for i in range(1, m):
            half = 1 << (i - 1)
            for j in range(n):
                max_values[j][i] = max_values[j][i - 1]
                min_values[j][i] = min_values[j][i - 1]
                if j + half < n:
                    max_values[j][i] = max(max_values[j][i], max_values[j + half][i - 1])
                    min_values[j][i] = min(min_values[j][i], min_values[j + half][i - 1])

        def get_min(left: int, right: int) -> int: # O(1) sparse table
            distance = right - left + 1
            k = distance.bit_length() - 1
            return min(min_values[left][k], min_values[right - (1 << k) + 1][k])
        
        def get_max(left: int, right: int) -> int: # O(1) sparse table
            distance = right - left + 1
            k = distance.bit_length() - 1
            return max(max_values[left][k], max_values[right - (1 << k) + 1][k])
 
        result = 0
        for divider in dividers: # sqrt(n)
            sortable = True
            prev_max = float("-inf")
            for right in range(divider - 1, n, divider): # n / k
                left = right - divider + 1
                sortable &= ((diff[right] - diff[left] <= 1) & (prev_max <= get_min(left, right)))
                if diff[right] - diff[left] == 1:
                    sortable &= nums[right] <= nums[left]
                
                prev_max = get_max(left, right)

            if sortable:
                result += divider
        
        return result