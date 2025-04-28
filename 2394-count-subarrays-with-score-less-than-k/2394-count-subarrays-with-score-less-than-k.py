class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # time: O(N)
        # space: O(1)
        # method: two pointers
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        right = 0
        cur = 0
        res = 0
        for left in range(n):
            # if left > right:
            #     right = left
            while right < n:
                sz = right - left + 1
                cur = nums[right]
                if left > 0:
                    cur -= nums[left - 1]
                cur *= sz
                if cur < k:
                    right += 1
                else:
                    break
            res += right - left
        return res