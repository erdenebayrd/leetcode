class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even, odd = 0, 0
        for x in nums:
            if x & 1:
                odd += 1
        for x in nums:
            if not x & 1:
                even += 1
        res = max(even, odd)
        oddEven = 0
        odd = True
        for x in nums:
            if odd is True:
                if x & 1:
                    oddEven += 1
                    odd = False
            else:
                if not x & 1:
                    oddEven += 1
                    odd = True
        res = max(oddEven, res)
        oddEven = 0
        odd = False
        for x in nums:
            if odd is True:
                if x & 1:
                    oddEven += 1
                    odd = False
            else:
                if not x & 1:
                    oddEven += 1
                    odd = True
        res = max(oddEven, res)
        return res