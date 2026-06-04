class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # time: O(N * max(len(words)))
        # space: O(N * max(len(words)))
        # method: DP
        
        words.sort(key=lambda word: len(word))
        dp = {}
        for word in words:
            dp[word] = 1
        for word in words:
            for i in range(len(word)):
                sub_word = word[0:i] + word[i + 1:]
                if sub_word in dp:
                    dp[word] = max(dp[word], dp[sub_word] + 1)
        result = 0
        for word in dp:
            result = max(result, dp[word])
        return result