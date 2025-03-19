class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def solve(x: int, lastDegree: int):
            if x <= 0:
                return True
            degree = int(math.log(x, 3) + 1e-10)
            if degree >= lastDegree:
                return False
            return solve(x - 3 ** degree, degree)
        return solve(n, int(math.log(1e7, 3)) + 1)