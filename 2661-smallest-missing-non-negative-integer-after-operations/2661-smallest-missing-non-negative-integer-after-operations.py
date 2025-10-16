class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        for i in range(n):
            cnt[nums[i] % value] += 1
        for i in range(n):
            if cnt[i % value] > 0:
                cnt[i % value] -= 1
            else:
                return i
        return n