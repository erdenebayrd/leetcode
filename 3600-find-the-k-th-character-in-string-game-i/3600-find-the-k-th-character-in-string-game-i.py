class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            add = ""
            for ch in word:
                add += chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
            word += add
        return word[k - 1]