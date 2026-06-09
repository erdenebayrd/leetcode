class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        # time: O(N)
        # space: O(K)
        # method: sliding window + counting
        count = defaultdict(int)
        n = len(candies)
        unique = 0
        result = 0
        for i in range(k, n):
            count[candies[i]] += 1
            if count[candies[i]] == 1:
                unique += 1
        result = unique
        for i in range(k, n):
            count[candies[i - k]] += 1
            if count[candies[i - k]] == 1:
                unique += 1
            count[candies[i]] -= 1
            if count[candies[i]] == 0:
                unique -= 1
            result = max(result, unique)
        return result