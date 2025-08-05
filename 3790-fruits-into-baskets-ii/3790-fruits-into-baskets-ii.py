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
                    break
            else: # if the for loop is not broken, this will work
                res += 1
        return res
        
