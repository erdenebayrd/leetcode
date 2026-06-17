class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        pos = {}
        for i in range(n):
            pos[stones[i]] = i
        
        @cache
        def solve(index: int, k: int) -> bool:
            if index == n - 1:
                return True
            units = []
            for i in range(-1, 2):
                if k + i > 0:
                    units.append(k + i)
            result = False
            for unit in units:
                value = stones[index] + unit
                if value in pos and pos[value] > index:
                    next_index = pos[value]
                    result |= solve(next_index, unit)
            return result
        
        return solve(0, 0)