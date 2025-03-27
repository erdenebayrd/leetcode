class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        pre, suf = defaultdict(int), defaultdict(int)
        for val in nums:
            suf[val] += 1
        for i, val in enumerate(nums):
            pre[val] += 1
            suf[val] -= 1
            preSize = i + 1
            sufSize = len(nums) - 1 - i
            if 2 * pre[val] > preSize and 2 * suf[val] > sufSize:
                # print(f"i: {i}, preVal: {pre[val]}, preSize: {preSize}")
                # print(f"i: {i}, sufVal: {suf[val]}, sufSize: {sufSize}")
                return i
        return -1