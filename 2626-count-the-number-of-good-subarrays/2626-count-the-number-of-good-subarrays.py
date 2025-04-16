class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # time: O(N)
        # space: O(N)
        # method: two pointers
        cnt = defaultdict(int)

        def nSum(n: int) -> int:
            return n * (n - 1) // 2

        def diff(prevCnt: int, curCnt: int) -> int:
            assert abs(prevCnt - curCnt) == 1
            return nSum(curCnt) - nSum(prevCnt)
        
        def calc(x: int, val: int) -> int:
            prevCnt = cnt[x]
            cnt[x] += val
            curCnt = cnt[x]
            return diff(prevCnt, curCnt)

        res, j, curK, n = 0, 0, 0, len(nums)
        for i in range(n):
            while j < n and curK < k:
                curK += calc(nums[j], 1)
                j += 1
            if curK >= k:
                res += n - j + 1
            else:
                break
            curK += calc(nums[i], -1)
        return res