class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # time: O(Sqrt(N) * (Q + N))
        # space: O(N)
        # method: Sqrt decomposition by Queries
        """
        check each queries
            - if step size of query is greater than or equal to Sqrt(N), Just simply update nums by the query O(Sqrt(N))
            - if step size of query is lower than Sqrt(N), group them by step size (at most Sqrt(N) groups will be created)
                - after grouping them by step size
                - iterate through each group and multiply [left] [diff] by "value" of the query, [right + step] divided by value (here we use Ferma's little theorom)
                - time complexity of this one would be Sqrt(N) "which is number of groups" * N "nums would be updated by [diff]"
        """
        n = len(nums)
        groups = defaultdict(list)
        sqrtN = int(n ** 0.5)
        mod = int(1e9 + 7)
        for left, right, step, value in queries: # O(Q)
            if step >= sqrtN: # apply at a time
                for i in range(left, right + 1, step): # O(Sqrt(N))
                    nums[i] = (nums[i] * value) % mod
            else: # step is too small to apply at a time
                groups[step].append([left, right, value])
        
        # size of "keys" groups at most Sqrt(N)
        for step in groups: # O(Sqrt(N))
            diff = [1] * n # O(N)
            for left, right, value in groups[step]: # O(Q)
                diff[left] = diff[left] * value
                endAt = left + ((right - left) // step) * step
                # here we use Ferma's little theorom for dividing
                # diff[endAt + step] = diff[endAt + step] / value
                # Ferma's little theorom: a ^ (prime - 1) = 1 module by "prime"
                # divided by "a" on both sides ( or we can say multiplied by a ^ -1 on both sides)
                # a ^ (prime - 1) * a ^ -1 = a ^ -1
                # a ^ (prime - 2) = a ^ -1
                # "a ^ (prime - 2)" this would be used here for dividing
                # diff[endAt + step] = diff[endAt + step] / value
                if endAt + step < n:
                    diff[endAt + step] = (diff[endAt + step] * pow(value, mod - 2, mod)) % mod
            for i in range(step, n): # O(N)
                diff[i] = diff[i] * diff[i - step] % mod
            for i in range(n): # O(N) updating "nums" array
                nums[i] = nums[i] * diff[i] % mod
        result = 0
        for number in nums:
            result ^= number
        return result