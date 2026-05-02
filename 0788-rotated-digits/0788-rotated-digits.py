class Solution:
    def rotatedDigits(self, n: int) -> int:
        """
        """
        # time: O(N * log10(N))
        # space: O(log10(N))
        # method: brute force
        result = 0
        for i in range(1, n + 1):
            number = str(i)
            if ("2" in number or "5" in number or "6" in number or "9" in number) and ("3" not in number and "4" not in number and "7" not in number):
                result += 1

        return result