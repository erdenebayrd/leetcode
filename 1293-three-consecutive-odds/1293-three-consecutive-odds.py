class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for i in range(2, len(arr)):
            cur = True
            for j in range(i - 2, i + 1):
                cur &= ((arr[j] & 1) == 1)
            if cur is True:
                return True
        return False