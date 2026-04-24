class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # time: O(N ^ 2)
        # space: O(N ^ 2)
        # method: DP
        n = len(piles)
        
        @cache
        def getRangeSum(left: int, right: int) -> int:
            if left > right:
                return 0
            if left == right:
                return piles[right]
            return piles[left] + piles[right] + getRangeSum(left + 1, right - 1)

        @cache
        def solve(left: int, right: int) -> int:
            if left > right:
                return 0
            if left == right:
                return piles[right]
            result = float('-inf')
            if (right - left + 1) & 1: # bob's turn
                result = max(result, piles[left] + getRangeSum(left + 1, right) - solve(left + 1, right)) # bob choose LEFT
                result = max(result, piles[right] + getRangeSum(left, right - 1) - solve(left, right - 1)) # bob choose RIGHT
            else: # alice's turn
                result = max(result, piles[left] + getRangeSum(left + 1, right) - solve(left + 1, right)) # alice choose LEFT
                result = max(result, piles[right] + getRangeSum(left, right - 1) - solve(left, right - 1)) # alice choose RIGHT
            return result
        
        alice = solve(0, n - 1)
        total = sum(piles)
        bob = total - alice
        return alice > bob