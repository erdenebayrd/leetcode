from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        cur = 0
        res = []
        n = len(nums)
        fq = defaultdict(int)
        topSl = SortedList([])
        restSl = SortedList([])

        def update(val: int, delta: int) -> None:
            nonlocal cur, fq, topSl, restSl, x
            if (fq[val], val) in topSl:
                topSl.remove((fq[val], val))
                cur -= val * fq[val]
            if (fq[val], val) in restSl:
                restSl.remove((fq[val], val))
            fq[val] += delta
            restSl.add((fq[val], val))
            if len(topSl) < x:
                topSl.add(restSl[-1])
                cur += restSl[-1][0] * restSl[-1][1]
                restSl.pop(-1) # not neccessary 
            elif topSl[0][0] < restSl[-1][0] or (topSl[0][0] == restSl[-1][0] and topSl[0][1] < restSl[-1][1]):
                cur -= topSl[0][0] * topSl[0][1]
                restSl.add(topSl[0])
                topSl.pop(0)
                topSl.add(restSl[-1])
                cur += restSl[-1][0] * restSl[-1][1]
                restSl.pop(-1) # not neccessary 
            # print("-" * 100)
            # print("restSl", restSl)
            # print("topSl", topSl)
            # print("-" * 100)
        
        for i in range(n - 1, n - k - 1, -1):
            update(nums[i], 1)
        res.append(cur)
        for i in range(n - k - 1, -1, -1):
            update(nums[i], 1)
            update(nums[i + k], -1)
            res.append(cur)
        return res[::-1]