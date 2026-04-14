class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        approach 1
        binary search by answer
        how much longer it can be
        can the length be "m"? we can check it by O(N * 26)
        total time: O(N * 26 * log N)
        space: O(N) for prefix sum of character occurrences
        method: binary search

        approach 2
        2 pointer/sliding window for searching every character
        s = "AABABBA", k = 1
        how many "A" we can find using k?
        how many "B" we can find using k?
        ....
        that would be total 26 times searching from the original string
        time: O(26 * N) -> O(N)
        space: O(1)
        method: 2 pointers / sliding window
        """

        # # time: O(N * 26)
        # # space: O(1)
        # # method: sliding window / 2 pointers

        # def longestSameCharacters(character: str) -> int:
        #     currentK = k
        #     left = 0
        #     result = 0
        #     for right in range(len(s)):
        #         if s[right] != character:
        #             currentK -= 1
        #         while left <= right and currentK < 0:
        #             if s[left] != character:
        #                 currentK += 1
        #             left += 1
        #         result = max(result, right - left + 1)
        #     return result
        
        # result = 0
        # for asciiCode in range(ord("A"), ord("Z") + 1): # O(26)
        #     character = chr(asciiCode)
        #     result = max(result, longestSameCharacters(character)) # O(N)
        # return result


        maxFrequency = 0
        left = 0
        n = len(s)
        result = 0
        count = defaultdict(int)
        for right in range(n):
            count[s[right]] += 1
            maxFrequency = max(maxFrequency, count[s[right]])
            while right - left + 1 - maxFrequency > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result