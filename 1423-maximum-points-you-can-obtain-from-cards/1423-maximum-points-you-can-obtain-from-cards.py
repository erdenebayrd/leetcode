from functools import lru_cache

class Solution:
    def maxScore(self, card_points: List[int], k: int) -> int:
        # # time: O(N ^ 2)
        # # space: O(N ^ 2)
        # # method: DP

        # n = len(card_points)
        # if k >= n:
        #     return sum(card_points)
        
        # @lru_cache(None)
        # def solve(left: int, right: int) -> int:
        #     length = right - left + 1
        #     taken = n - length
        #     if taken == k:
        #         return 0
        #     return max(card_points[left] + solve(left + 1, right), card_points[right] + solve(left, right - 1))
        
        # solve.cache_clear()

        # return solve(0, n - 1)

        """
        lets think in this way

        since we have to take exactly k cards from the given card list
        and we only can chose from left or right
        
        meaning

            * we can chose 0 cards from left, k cards from right
            * 1 card from left, k - 1 cards from right
            * .....
            * k cards from left, 0 cards from right

        we just take maximum of them

        why it works, because there is no difference between choosing orders
        at the end of the day we have to choose exactly k cards from left or right (can be divided)
        there is no different between first take from left and second from right
        or 
        first from right, second from left
        sum of those values are same

        we can just prepare prefix sum and suffix sum get range sum by O(1)
        """
        # time: O(N + K)
        # space: O(N)
        # method: prefix sum + greedy
        n = len(card_points)
        if k >= n:
            return sum(card_points)

        # prefix = [0] * n
        # prefix[0] = card_points[0]
        # for i in range(1, n):
        #     prefix[i] = prefix[i - 1] + card_points[i]
        
        # def get_range_sum(left: int, right: int) -> int:
        #     if left > right:
        #         return 0
        #     if left == 0:
        #         return prefix[right]
        #     return prefix[right] - prefix[left - 1]
        
        # result = float('-inf')
        # for take_left in range(k + 1):
        #     # take_left is number of cards taken from left side
        #     take_right = k - take_left
        #     score_left = get_range_sum(0, take_left - 1)
        #     score_right = get_range_sum(n - take_right, n - 1)
        #     total_score = score_left + score_right
        #     result = max(result, total_score)
        # return result


        """
            actually k is fixed number we can use sliding window
            then space become O(1)
        """
        # time: O(K)
        # space: O(1)
        # method: sliding window + greedy

        score_left = 0
        score_right = sum(card_points[n - k:])
        total = score_left + score_right
        result = total
        for take_left in range(1, k + 1):
            # number of elements from left side
            score_left += card_points[take_left - 1]
            score_right -= card_points[n - k + take_left - 1]
            total = score_left + score_right
            result = max(result, total)
        return result