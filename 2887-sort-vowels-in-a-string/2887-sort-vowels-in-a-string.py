class Solution:
    def sortVowels(self, s: str) -> str:
        # time: O(N)
        # space: O(N)
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        t, w = [], ""
        for i in range(len(s)):
            if s[i] in vowels:
                t.append('A')
                w += s[i]
            else:
                t.append(s[i])
        w = sorted(w)
        # print(w)
        curIdx = 0
        for vowel in w:
            while curIdx < len(t) and t[curIdx] != 'A':
                curIdx += 1
            t[curIdx] = vowel
            curIdx += 1
        # print(t)
        return "".join(t)