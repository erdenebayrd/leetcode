class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            cnt = [0] * 26
            for ch in s:
                x = ord(ch) - ord('a')
                cnt[x] += 1
            cnt = tuple(cnt)
            if cnt not in anagrams:
                anagrams[cnt] = []
            anagrams[cnt].append(s)
        
        res = []
        for key in anagrams:
            res.append(anagrams[key])
        return res