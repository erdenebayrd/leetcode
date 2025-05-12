class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        cnt = Counter(digits)
        res = []
        for i in range(100, 1000):
            if i & 1:
                continue
            cur = []
            for ch in str(i):
                cur.append(int(ch))
            cur = Counter(cur)
            flag = True
            for key in cur:
                flag &= cnt[key] >= cur[key]
            if flag is True:
                res.append(i)
        return res