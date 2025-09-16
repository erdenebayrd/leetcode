class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = [x for x in nums]
        latestIdx = 0
        for i in range(1, len(nums)):
            cur = nums[i]
            while latestIdx >= 0:
                _gcd = gcd(cur, stack[latestIdx])
                if _gcd == 1:
                    break
                lcm = cur * stack[latestIdx] // _gcd
                cur = lcm
                latestIdx -= 1
            latestIdx += 1
            stack[latestIdx] = cur
        return stack[:latestIdx + 1]