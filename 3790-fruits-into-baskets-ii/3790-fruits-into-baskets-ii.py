class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # time: O(N^2)
        # space: O(N)
        # method: brute force
        n = len(fruits)
        res = 0
        for i in range(n): # fruits
            for j in range(n): # baskets
                if fruits[i] <= baskets[j]:
                    baskets[j] = 0
                    fruits[i] = 0
                    res += 1
                    break
        return n - res
