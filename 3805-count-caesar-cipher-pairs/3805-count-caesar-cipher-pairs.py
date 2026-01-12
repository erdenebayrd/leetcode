class Solution:
    def countPairs(self, words: List[str]) -> int:
        # 1 <= n == words.length <= 10^5
        # 1 <= m == words[i].length <= 10^5
        ### 1 <= n * m <= 10^5
        chars = [chr(ch + ord('a')) for ch in range(26)]
        # print(chars)
        def convert(word: str) -> str:
            diff = []
            for i in range(1, len(word)):
                diff.append((ord(word[i]) - ord(word[i - 1])) % 26)
            res = "a"
            for x in diff:
                # db => -2 => -2 % 26 = 24 => ay
                res += chars[x]
            return res
        
        res = 0
        cnt = {}
        for word in words:
            convertedWord = convert(word)
            if convertedWord in cnt:
                res += cnt[convertedWord]
            if convertedWord not in cnt:
                cnt[convertedWord] = 0
            cnt[convertedWord] += 1
        return res