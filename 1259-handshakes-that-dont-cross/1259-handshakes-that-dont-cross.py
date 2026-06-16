class Solution:
    def numberOfWays(self, num_people: int) -> int:
        """
        2 -> 1
        4 -> 2
        6 -> 

           1  2 
         3     4
           5  6
        1 * 1 + 2 + 2 = 5

        n

        (n - 2) * 2 + f(n - 4) * f(2) + f(n - 6) * f(4) + f(6) * f(n - 8)

        """
        mod = 1_000_000_007

        @cache
        def solve(n: int) -> int:
            if n <= 2:
                return n // 2
            result = (solve(n - 2) * 2) % mod
            for i in range(4, n - 1, 2):
                left = i - 2
                right = n - i
                result = (result + (solve(left) * solve(right)) % mod) % mod
            return result

        result = solve(num_people)
        return result