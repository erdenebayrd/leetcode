class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        digits = [chr(ord('0') + x) for x in range(10)]
        print(digits)
        consonants = []
        for ch in range(ord('a'), ord('z') + 1):
            x = chr(ch)
            if x in vowels:
                continue
            consonants.append(x)
        for ch in range(ord('A'), ord('Z') + 1):
            x = chr(ch)
            if x in vowels:
                continue
            consonants.append(x)
        chars = []
        for ch in vowels:
            chars.append(ch)
        for ch in digits:
            chars.append(ch)
        for ch in consonants:
            chars.append(ch)
        if len(word) < 3:
            return False
        for ch in word:
            if ch not in chars:
                return False
        atLeastOneVowel = False
        for ch in vowels:
            atLeastOneVowel |= (ch in word)
        if atLeastOneVowel is False:
            return False
        atLeastOneConsonant = False
        for ch in consonants:
            atLeastOneConsonant |= (ch in word)
        if atLeastOneConsonant is False:
            return False
        return True
        