class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        beginZero = []
        beginOne = []
        n = len(groups)
        for i in range(n):
            if len(beginZero) == 0 and groups[i] == 0:
                beginZero.append(i)
            if len(beginOne) == 0 and groups[i] == 1:
                beginOne.append(i)
            if len(beginZero) > 0 and groups[beginZero[-1]] != groups[i]:
                beginZero.append(i)
            if len(beginOne) > 0 and groups[beginOne[-1]] != groups[i]:
                beginOne.append(i)
        res = []
        if len(beginZero) > len(beginOne):
            for idx in beginZero:
                res.append(words[idx])
        else:
            for idx in beginOne:
                res.append(words[idx])
        return res