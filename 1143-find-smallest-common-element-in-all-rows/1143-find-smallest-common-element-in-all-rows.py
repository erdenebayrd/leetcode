class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # time: O(N ^ 2)
        # space: O(N ^ 2)
        # method: brute force
        n = len(mat)
        row = [{} for _ in range(n)]
        for i in range(n):
            for x in mat[i]:
                row[i][x] = True

        def check(x: int) -> bool:
            for i in range(n):
                if x not in row[i]:
                    return False
            return True

        for x in mat[0]:
            if check(x) is True:
                return x
        return -1