class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        cnt = defaultdict(int)
        seen = set()
        cnt[nums[0]] = 1
        tmp = 0
        for i in range(n):
            if nums[i] == 0:
                tmp += 1
        if tmp == n:
            return [[0, 0, 0]]
        for i in range(1, n):
            for j in range(i + 1, n):
                x = -nums[i] - nums[j]
                if cnt[x] > 0:
                    arr = tuple(sorted([x, nums[i], nums[j]]))
                    if arr not in seen:
                        seen.add(arr)
            cnt[nums[i]] += 1
        
        res = []
        for item in seen:
            res.append(list(item))
        return res