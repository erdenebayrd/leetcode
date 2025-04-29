class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = max(nums)
        res, cnt, left = 0, 0, -1
        for right in range(n):
            if nums[right] == mx:
                cnt += 1
            if cnt < k:
                continue
            if nums[right] == mx:
                left += 1
                while nums[left] != mx:
                    left += 1
            res += left + 1
        return res