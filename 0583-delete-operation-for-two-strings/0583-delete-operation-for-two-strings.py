from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n = len(word1)
        m = len(word2)
        
        @lru_cache(None)
        def cost(first_pointer: int, second_pointer: int) -> int:
            if first_pointer == n and second_pointer == m:
                return 0
            
            # first_pointer = n
            # when second_pointer = 3
            
            if first_pointer >= n:
                return m - second_pointer
            if second_pointer >= m:
                return n - first_pointer
            
            if word1[first_pointer] == word2[second_pointer]:
                return cost(first_pointer + 1, second_pointer + 1)
            else:
                return 1 + min(cost(first_pointer + 1, second_pointer), cost(first_pointer, second_pointer + 1))
    
        result = cost(0, 0)

        cost.cache_clear()
        return result