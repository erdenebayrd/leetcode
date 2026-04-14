class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # time: O(N * target)
        # space: O(N * target)
        # method: DP
        n = len(types)
        mod = int(1e9 + 7)

        @cache
        def solve(index: int, target: int) -> int:
            if target == 0:
                return 1
            if target < 0 or index >= n:
                return 0
            result = solve(index + 1, target) # meaning no score from this type of questions
            count, mark = types[index]
            result = (result + solve(index, target - mark)) % mod
            result = (result - solve(index + 1, target - (count + 1) * mark)) % mod
            return result
        
        return solve(0, target)
