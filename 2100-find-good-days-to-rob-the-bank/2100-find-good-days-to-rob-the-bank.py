class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return [day for day in range(n)]
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = int(security[i - 1] >= security[i]) + prefix[i - 1]
        suffix[n - 1] = 1
        for i in range(n - 2, -1, -1):
            suffix[i] = int(security[i] <= security[i + 1]) + suffix[i + 1]
        
        def rangeSumPrefix(l: int, r: int) -> int:
            if l == 0:
                return prefix[r]
            return prefix[r] - prefix[l - 1]
        
        def rangeSumSuffix(l: int, r: int) -> int:
            if r == n - 1:
                return suffix[l]
            return suffix[l] - suffix[r + 1]
        # print(prefix)
        # print(suffix)
        goodDays = []
        for day in range(time, n - time):
            if rangeSumPrefix(day - time + 1, day) == time and rangeSumSuffix(day, day + time - 1) == time:
                goodDays.append(day)
        return goodDays