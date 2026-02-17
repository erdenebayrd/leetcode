from math import gcd
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # [1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5 ]
        # 1: 6
        # 5: 9
        # x = 3, [111], [111], [555], [555], [555]

        if len(deck) == 0:
            return False
        
        counter = Counter(deck)
        greatestCommonDivisor = 0
        for _, count in counter.items():
            greatestCommonDivisor = gcd(greatestCommonDivisor, count)
        return greatestCommonDivisor > 1