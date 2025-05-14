import numpy as np

class Solution:
    def __init__(self):
        self.__MOD = int(1e9 + 7)

    def matrix_power_mod(self, A, power):
        result = np.identity(A.shape[0], dtype=object)
        A = A % self.__MOD
        while power > 0:
            if power & 1:
                result = np.matmul(result, A) % self.__MOD
            A = np.matmul(A, A) % self.__MOD
            power >>= 1
        return result

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        cnt = Counter(s)
        F = np.array([[cnt[chr(idx + ord('a'))]] for idx in range(26)])
        # print(F)
        
        T = np.zeros((26, 26), dtype=object)
        for i in range(26):
            for j in range(nums[i]):
                T[(i + j + 1) % 26, i] = 1
        # print(T)
        
        # T = np.linalg.matrix_power(T, t)
        T = self.matrix_power_mod(T, t)
        result = T @ F % self.__MOD
        # print(result)
        return result.sum() % self.__MOD