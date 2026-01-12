class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        # time: O(32 * N * Log N)
        # space: O(N)
        def bit(num: int, i: int) -> int:
            return (num >> i) & 1

        def cost(num: int, cand: int) -> int: # O(32)
            for i in range(31, -1, -1):
                if bit(num, i) == 1 and bit(cand, i) == 1:
                    num ^= (1 << i)
                    cand ^= (1 << i)
                elif bit(num, i) == 1 and bit(cand, i) == 0:
                    num ^= (1 << i)
                elif bit(num, i) == 0 and bit(cand, i) == 1:
                    return (1 << i) - num + ((1 << i) ^ cand)
            return 0


        res = 0
        for i in range(31, -1, -1):
            cand = res | (1 << i)
            costs = []
            for num in nums: 
                costs.append(cost(num, cand))
            costs.sort() # O(N * LogN)
            if sum(costs[:m]) <= k:
                res = cand
        return res