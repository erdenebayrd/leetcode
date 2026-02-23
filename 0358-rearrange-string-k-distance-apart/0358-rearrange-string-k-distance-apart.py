class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        result = ""
        counter = Counter(s)
        def nextChar() -> str: # O(26)
            # pick a character which is not in last k - 1 elements of re-arranged string "result" with maximum occurences
            lastChars = set()
            current = k - 1
            index = len(result) - 1
            while index >= 0 and current > 0:
                lastChars.add(result[index])
                index -= 1
                current -= 1

            occurrences = 0
            pickedChar = ""
            for ch in counter:
                if ch not in lastChars:
                    if occurrences < counter[ch]:
                        occurrences = counter[ch]
                        pickedChar = ch
            return pickedChar
        
        n = len(s)
        result = ""
        for i in range(n):
            picked = nextChar()
            if picked == "":
                return ""
            result += picked
            counter[picked] -= 1
        return result