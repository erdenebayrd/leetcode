class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # time: O(N ^ 2)
        # space: O(N ^ 2) to O(N)
        # method: n pointers
        n = len(mat)
        m = len(mat[0])
        pointers = [0] * n
        
        def check() -> bool: # O(N)
            x = mat[0][pointers[0]]
            for row, idx in enumerate(pointers):
                if mat[row][idx] != x:
                    return False
            return True
        
        def getMax() -> int: # O(N)
            x = mat[0][pointers[0]]
            for row, idx in enumerate(pointers):
                x = max(x, mat[row][idx])
            return x

        while True:
            if check() is True: # O(N)
                return mat[0][pointers[0]]
            x = getMax() # O(N)
            for i in range(n): # O(N ^ 2)
                idx = pointers[i]
                while idx < m and mat[i][idx] < x:
                    idx += 1
                pointers[i] = idx
            if max(pointers) >= m:
                return -1