class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = []
        for x in nums:
            if len(arr) == 0 or arr[-1] != x:
                arr.append(x)
        res = 0
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1] or arr[i - 1] > arr[i] < arr[i + 1]:
                res += 1
        return res