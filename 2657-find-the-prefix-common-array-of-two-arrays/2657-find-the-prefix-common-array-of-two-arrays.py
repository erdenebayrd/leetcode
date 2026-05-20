from collections import defaultdict

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # time: O(N)
        # space: O(N)
        # method: frequency
        frequency = defaultdict(int)
        n = len(A)
        counter = 0
        result = [0] * n
        for i in range(n):
            frequency[A[i]] += 1
            if frequency[A[i]] == 2:
                counter += 1
            frequency[B[i]] += 1
            if frequency[B[i]] == 2:
                counter += 1
            result[i] = counter
        return result