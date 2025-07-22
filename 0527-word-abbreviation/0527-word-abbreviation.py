class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        n = len(words)

        def abb(s: str, k: int) -> str:
            if len(s) <= k + 2:
                return s
            return s[:k] + f"{len(s) - k - 1}" + s[-1]

        def solve(idxs, k: int):
            s = {}
            for idx in idxs:
                word = abb(words[idx], k)
                if word not in s:
                    s[word] = []
                s[word].append(idx)
            res = {}
            ans = []
            for word in s:
                if len(s[word]) == 1:
                    res[word] = s[word][0]
                else:
                    ans.append(solve(s[word], k + 1))
            # print(ans)
            for i in range(len(ans)):
                for word in ans[i]:
                    assert word not in res
                    res[word] = ans[i][word]
            return res
        
        res = solve([x for x in range(n)], 1)
        ans = [""] * n
        for word in res:
            ans[res[word]] = word
        # for i in range(n):
        #     if len(ans[i]) == len(words[i]):
        #         ans[i] = words[i]
        return ans