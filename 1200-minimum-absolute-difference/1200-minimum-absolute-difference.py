class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        mn = float('inf')
        for i in range(1, n):
            mn = min(mn, arr[i] - arr[i - 1])
        res = []
        for i in range(1, n):
            if arr[i] - arr[i - 1] == mn:
                res.append([arr[i - 1], arr[i]])
        return res