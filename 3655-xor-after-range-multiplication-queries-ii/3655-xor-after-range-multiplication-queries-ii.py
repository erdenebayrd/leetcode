class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # time: O(Sqrt(N) * Q)
        # space: O(N)
        # method: Sqrt decomposition
        n = len(nums)
        mod = int(1e9 + 7)
        sqrtSize = int(n ** 0.5)
        group = defaultdict(list)
        for left, right, step, value in queries: # O( Q * Sqrt(N) )
            if step < sqrtSize:
                group[step].append([left, right, value])
            else:
                for index in range(left, right + 1, step):
                    nums[index] = (nums[index] * value) % mod
        
        for step in range(1, sqrtSize): # O( Sqrt(N) * (Q + N) )
            if not group[step]:
                continue
            diff = [1] * n
            for left, right, value in group[step]:
                diff[left] = (diff[left] * value) % mod
                end = left + ((right - left) // step) * step + step
                if end < n:
                    diff[end] = (diff[end] * pow(value, mod - 2, mod)) % mod
            for index in range(step, n):
                diff[index] = (diff[index] * diff[index - step]) % mod
            for index in range(n):
                nums[index] = (nums[index] * diff[index]) % mod
        result = 0
        for i in range(n):
            result ^= nums[i]
        return result
