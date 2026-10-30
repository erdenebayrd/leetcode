class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # time: O(n * 2 ^ n)
        # space: O(n * 2 ^ n)
        # method: backtrack
        candidates.sort()
        n = len(candidates)
        combinations = []
        current = []
        def backtrack(index: int, target: int) -> None:
            if target == 0:
                combinations.append(current[:])
            
            if target <= 0 or index >= n:
                return
            
            # take
            current.append(candidates[index])
            backtrack(index + 1, target - candidates[index])
            current.pop()
        
            # skip
            while index + 1 < n and candidates[index] == candidates[index + 1]:
                index += 1
            
            backtrack(index + 1, target)
        
        backtrack(0, target)
        return combinations