class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        import numpy as np
        m1 = np.array(mat1)
        m2 = np.array(mat2)
        res = np.dot(m1, m2)
        return res.tolist()