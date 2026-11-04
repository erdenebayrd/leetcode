from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        # time: O(N log x + N * K)
        # space: O(N)
        # method: DP + sorted list
        n = len(nums)
        inf = float('inf')
        
        first_half = SortedList([])
        second_half = SortedList([])
        sums = [0, 0] # first half sum, second half sum
        
        def balance() -> None: # O(log x) amortized
            is_odd = x & 1
            while len(first_half) != len(second_half) - is_odd:
                if len(first_half) > len(second_half) - is_odd:
                    sums[1] += first_half[-1]
                    second_half.add(first_half[-1])
                    sums[0] -= first_half[-1]
                    first_half.remove(first_half[-1])
                elif len(first_half) < len(second_half) - is_odd:
                    sums[0] += second_half[0]
                    first_half.add(second_half[0])
                    sums[1] -= second_half[0]
                    second_half.remove(second_half[0])

        def add(value: int) -> None: # O(log x)
            if not first_half and not second_half: # both empty
                second_half.add(value)
                sums[1] += value
            elif not first_half: # only first half is empty
                if second_half[0] <= value:
                    second_half.add(value)
                    sums[1] += value
                else:
                    first_half.add(value)
                    sums[0] += value
            else: # both not empty OR only second half is empty
                if value <= first_half[-1]:
                    first_half.add(value)
                    sums[0] += value
                else:
                    second_half.add(value)
                    sums[1] += value
        
        def remove(value: int) -> None: # O(log x)
            if value in first_half:
                first_half.remove(value)
                sums[0] -= value
            else:
                second_half.remove(value)
                sums[1] -= value

        def calc_cost() -> int:
            result = inf
            median = second_half[0]
            result = min(result, sums[1] - median * len(second_half) + median * len(first_half) - sums[0])
            if len(first_half) == len(second_half): # meaning X is EVEN
                median = first_half[-1]
                result = min(result, sums[1] - median * len(second_half) + median * len(first_half) - sums[0])
            return result

        for i in range(x):
            add(nums[i])
        
        balance() # balance sorted lists

        cost = [inf] * n
        cost[x - 1] = calc_cost()

        for i in range(x, n):
            add(nums[i])
            remove(nums[i - x])
            balance()
            cost[i] = calc_cost()

        # print(cost)

        dp = [[inf] * n for _ in range(k + 1)]
        for i in range(n):
            dp[0][i] = 0
            dp[1][i] = cost[i]
            if i - 1 >= 0:
                dp[1][i] = min(dp[1][i], dp[1][i - 1])
        
        for i in range(2, k + 1):
            for j in range(x, n):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - x] + cost[j])
        
        return min(dp[k])