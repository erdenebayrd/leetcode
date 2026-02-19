from functools import cache

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # time: O(N * M) ene deer bas aldsan N ^ 2 bolgochood N ^ 3 bolgoh yostoi l doo
        # space: O(N * M) ene deer aldsan, ehleed O(N) gecheed teriigee zasaagui orhiod yavtsan!!!
        # arr1 = sentence1.split()
        # arr2 = sentence2.split()

        # n = len(arr1)
        # m = len(arr2)

        # @cache
        # def isValid(first: int, second: int, chances: int) -> bool:
        #     if chances < 0:
        #         return False

        #     if first == n:
        #         if chances > 0:
        #             return True
        #         else:
        #             return second == m
            
        #     if second == m:
        #         if chances > 0:
        #             return True
        #         else:
        #             return first == n

        #     result = False
        #     if arr1[first] == arr2[second]:
        #         result |= isValid(first + 1, second + 1, chances)
            
        #     for right in range(first, n):
        #         result |= isValid(right + 1, second, chances - 1)
            
        #     for right in range(second, m):
        #         result |= isValid(first, right + 1, chances - 1)

        #     return result
        
        # return isValid(0, 0, 1)


        # # "qbaVXO Msgr aEWD v ekcb"
        # # "Msgr aEWD ekcb"

        # # |
        # # |
        # # |
        # # V

        # # "Msgr aEWD v ekcb"
        # # "Msgr aEWD ekcb"

        # # |
        # # |
        # # |
        # # V

        # # "v ekcb"
        # # "ekcb"

        arr1 = sentence1.split()
        arr2 = sentence2.split()

        n = len(arr1)
        m = len(arr2)

        # print(arr1)
        # print(arr2)

        left = 0
        while left < n and left < m and arr1[left] == arr2[left]:
            left += 1
        
        right1 = n - 1
        right2 = m - 1
        while right1 >= 0 and right2 >= 0 and arr1[right1] == arr2[right2]:
            right1 -= 1
            right2 -= 1
        
        # print(left, right1, right2)
        if left > right1 or left > right2:
            return True
        return False