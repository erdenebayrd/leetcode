class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2 * k:
            return 0
        mod = int(1e9 + 7)
        n = len(nums)
        @cache
        def solve(index: int, k: int) -> int:
            if k <= 0:
                return 0
            if index >= n:
                return 1
            result = solve(index + 1, k)
            result += solve(index + 1, k - nums[index])
            return result % mod
        # print(solve(0, k))
        result = (pow(2, n, mod) - solve(0, k) * 2) % mod
        # result = (1 << n) - solve(0, k) * 2
        # print(result)
        return result % mod
        # bitsum = [0] * (1 << n)
        # for i in range(1, 1 << n):
        #     index = i.bit_length() - 1
        #     bitsum[i] = bitsum[i ^ (1 << index)] + nums[index]
        # total = sum(nums)
        # result = 0
        # for i in range(len(bitsum)):
        #     first = bitsum[i]
        #     second = total - first
        #     print(first, second)
        #     if first >= k and second >= k:
        #         result += 1
        # return result