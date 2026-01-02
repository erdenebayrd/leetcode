class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        uniq = set()
        for x in nums:
            if x not in uniq:
                uniq.add(x)
            else:
                return x