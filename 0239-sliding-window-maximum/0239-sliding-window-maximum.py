class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()

        n = len(nums)
        for i in range(n):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            if dq and dq[0] <= i - k:
                dq.popleft()

            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
            