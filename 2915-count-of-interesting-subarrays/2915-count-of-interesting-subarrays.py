class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res, cnt = 0, 0
        cntDict = defaultdict(int)
        cntDict[0] = 1
        for x in nums:
            if x % modulo == k:
                cnt += 1
            rem = cnt % modulo
            needed = (rem - k + modulo) % modulo
            
            res += cntDict[needed]
            cntDict[rem] += 1
        return res