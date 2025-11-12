class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        _gcd = 0
        cnt = 0
        for x in nums:
            if x == 1:
                cnt += 1
            _gcd = gcd(_gcd, x)
        if cnt > 0:
            return n - cnt
        if _gcd > 1:
            return -1
        
        res = n
        for i in range(n):
            _gcd = 0
            for j in range(i, n):
                _gcd = gcd(_gcd, nums[j])
                if _gcd == 1:
                    res = min(res, j - i + 1)
                    break
        return res - 1 + n - 1