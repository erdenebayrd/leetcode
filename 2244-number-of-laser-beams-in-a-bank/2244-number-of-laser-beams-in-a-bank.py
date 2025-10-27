class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        pre = 0
        for row in bank:
            cur = row.count('1')
            if cur == 0:
                continue
            res += pre * cur
            pre = cur
        return res