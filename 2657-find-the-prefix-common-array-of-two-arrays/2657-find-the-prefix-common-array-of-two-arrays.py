from collections import defaultdict

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # time: O(N)
        # space: O(1)
        # method: frequency
        frequency = 0
        n = len(A)
        counter = 0
        result = [0] * n
        for i in range(n):
            value = A[i]
            frequency ^= (1 << value)
            if (frequency >> value) & 1 == 0:
                counter += 1
            value = B[i]
            frequency ^= (1 << value)
            if (frequency >> value) & 1 == 0:
                counter += 1
            result[i] = counter
        return result