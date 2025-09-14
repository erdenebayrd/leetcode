class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        orig = {}
        low = {}
        vow = {}
        for word in wordlist:
            orig[word] = word
            if word.lower() not in low:
                low[word.lower()] = []
            low[word.lower()].append(word)
            cur = ""
            for ch in word.lower():
                if ch in vowels:
                    cur += "@"
                else:
                    cur += ch
            if cur not in vow:
                vow[cur] = []
            vow[cur].append(word)
        # print(vow)
        for i, query in enumerate(queries):
            if query in orig:
                res.append(query)
            elif query.lower() in low:
                res.append(low[query.lower()][0])
            else:
                cur = ""
                for ch in query.lower():
                    if ch in vowels:
                        cur += "@"
                    else:
                        cur += ch
                cur = cur.lower()
                if cur not in vow:
                    res.append("")
                else:
                    res.append(vow[cur][0])
        return res