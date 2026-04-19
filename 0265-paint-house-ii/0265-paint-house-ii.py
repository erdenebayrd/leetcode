class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # time: O(N * K ^ 2)
        # space: O(N * K)
        # method: DP
        n = len(costs)
        k = len(costs[0])
        @cache
        def solve(prevColor: int, index: int) -> int:
            if index >= n:
                return 0
            result = float('inf')
            for color in range(k):
                if color == prevColor:
                    continue
                result = min(result, costs[index][color] + solve(color, index + 1))
            return result
        return solve(-1, 0)