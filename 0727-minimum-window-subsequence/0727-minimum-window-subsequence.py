class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        """
        subsequence means
        from some contigious substring of s1 that can cover all chars in s2 with it's order
        meaning s2 can be derived from substring of s1 without changing it's order
        
            * the first thing is to find minimum length of substring of s1 that covers s2
            * then find starting index
        
        we can use DP in here to dinf minimum length
        2d DP
        dp[i][j] "i" index represent s1's index, "j" represent s2's index
        until index "i" of s1 and until index "j" of s2 
        what is the minimum length
        for example:
            s1 = "abcdebdde", s2 = "bde"
               
               a b c d e b d d e
            b  f 1 2 3 4 1 2 3 4

            d  f f f 3 4 5 2 3 4
            
            e  f f f f 4 5 6 7 4
        """
        # time: O(N * M) N is length of s1 and M is length of s2
        # space: O(N * M)
        # method: DP
        n = len(s1)
        m = len(s2)
        dp = [[float('inf')] * n for _ in range(m)]
        for i in range(n):
            if s1[i] == s2[0]:
                dp[0][i] = 1
            else:
                if i > 0:
                    dp[0][i] = dp[0][i - 1] + 1

        for row in range(1, m):
            for col in range(1, n):
                if s2[row] == s1[col]:
                    dp[row][col] = min(dp[row][col], dp[row - 1][col - 1] + 1)
                else:
                    dp[row][col] = min(dp[row][col], dp[row][col - 1] + 1)
        
        # for i in range(m):
        #     print(dp[i])

        length = min(dp[-1])
        if length == float('inf'):
            return ""
        start = float('inf')
        for col in range(n):
            if length == dp[-1][col]:
                start = col - length + 1
                break
        return s1[start:start+length]