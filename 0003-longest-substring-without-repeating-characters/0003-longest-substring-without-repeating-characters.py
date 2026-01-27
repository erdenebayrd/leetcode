from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        leftIndex = 0
        characterOccurences = defaultdict(int)
        n = len(s)
        for rightIndex in range(n):
            characterOccurences[s[rightIndex]] += 1
            while leftIndex < n and characterOccurences[s[rightIndex]] > 1:
                characterOccurences[s[leftIndex]] -= 1
                leftIndex += 1
            answer = max(answer, rightIndex - leftIndex + 1)
            print(leftIndex, rightIndex)
        return answer
