class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
        for key in cnt:
            if cnt[key] & 1:
                return False
        return True