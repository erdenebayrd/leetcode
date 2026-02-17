from math import gcd
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # [1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5 ]
        # 1: 6
        # 5: 9
        # x = 3, [111], [111], [555], [555], [555]

        # tc: O(N + K * log M) N number of elements in deck, K is number of unique elements, M is maximum counted value
        # sc: O(K)
        if len(deck) == 0:
            return False
        
        counter = Counter(deck)
        greatestCommonDivisor = 0
        for _, count in counter.items():
            greatestCommonDivisor = gcd(greatestCommonDivisor, count)
        return greatestCommonDivisor > 1