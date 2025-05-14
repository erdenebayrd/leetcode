import numpy as np

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 1_000_000_007
        cnt = Counter(s)
        F = np.array([[cnt[chr(idx + ord('a'))]] for idx in range(26)])
        # print(F)
        
        T = np.zeros((26, 26), dtype=object)
        for i in range(26):
            for j in range(nums[i]):
                T[(i + j + 1) % 26, i] = 1
        # print(T)
        
        def matrix_power_mod(A, power, mod):
            result = np.identity(A.shape[0], dtype=object)
            A = A % mod
            while power > 0:
                if power & 1:
                    result = np.matmul(result, A) % mod
                A = np.matmul(A, A) % mod
                power //= 2
            return result
        
        # T = np.linalg.matrix_power(T, t)
        T = matrix_power_mod(T, t, MOD)
        result = T @ F % MOD
        # print(result)
        return result.sum() % MOD