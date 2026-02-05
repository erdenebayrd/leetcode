from functools import cache

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        @cache
        def solve(index: int) -> int:
            if index >= n:
                return 0 # height
            width = 0
            height = 0
            cost = float('inf')
            for endIndex in range(index, n):
                currentBookWidth, currentBookHeight = books[endIndex]
                width += currentBookWidth
                height = max(height, currentBookHeight)
                if width > shelfWidth:
                    break
                cost = min(cost, height + solve(endIndex + 1))
            return cost
            
        return solve(0)