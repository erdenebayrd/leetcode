class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        cnt = Counter(nums)
        arr = [cnt[key] for key in cnt]
        arr.sort(reverse=True)
        cnt = [0] * arr[0]
        idx = 0
        for x in arr:
            while x > 0:
                x -= 1
                cnt[idx] += 1
                idx = (idx + 1) % len(cnt)
        return min(cnt) >= k