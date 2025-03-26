class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n, m = len(word), len(abbr)
        i = j = 0
        while True:
            while i < n and j < m and word[i] == abbr[j]:
                i += 1
                j += 1
            if i == n and j == m:
                return True
            num = ""
            while j < m and '0' <= abbr[j] <= '9':
                num += abbr[j]
                j += 1
            if num == "" or num[0] == '0':
                return False
            i += int(num)
            if i == n and j == m:
                return True
            if i > n:
                return False