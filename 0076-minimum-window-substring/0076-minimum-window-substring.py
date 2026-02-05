class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countPattern = Counter(t)
        countCurrentWindow = Counter()
        matchedLength = 0
        leftIndex = 0
        minimumLength = float('inf')
        pointers = []
        for rightIndex in range(len(s)):
            currentChar = s[rightIndex]
            if currentChar not in countPattern:
                continue
            if countCurrentWindow[currentChar] < countPattern[currentChar]:
                matchedLength += 1
            countCurrentWindow[currentChar] += 1
            
            if matchedLength == len(t):
                while leftIndex < len(s) and (s[leftIndex] not in countPattern or countCurrentWindow[s[leftIndex]] - 1 >= countPattern[s[leftIndex]]):
                    countCurrentWindow[s[leftIndex]] -= 1
                    leftIndex += 1
                currentLength = rightIndex - leftIndex + 1
                if currentLength < minimumLength:
                    minimumLength = currentLength
                    pointers = [leftIndex, rightIndex]
                countCurrentWindow[s[leftIndex]] -= 1
                matchedLength -= 1
                leftIndex += 1
        if len(pointers) == 0:
            return ""
        leftIndex, rightIndex = pointers
        return s[leftIndex:rightIndex + 1]