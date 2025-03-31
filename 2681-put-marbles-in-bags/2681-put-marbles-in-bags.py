class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # time: O(N*LogN)
        # space: O(N)
        n = len(weights)
        arr = []
        for i in range(1, n):
            arr.append(weights[i] + weights[i - 1])
        arr.sort()
        print(arr)
        mn = 0
        for i in range(k - 1):
            mn += arr[i]
        mx = 0
        n = len(arr)
        for i in range(n - 1, n - k, -1):
            mx += arr[i]
        return mx - mn