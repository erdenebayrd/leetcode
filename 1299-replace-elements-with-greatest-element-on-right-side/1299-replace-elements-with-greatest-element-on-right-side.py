class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # time: O(N)
        # space: O(1)
        # method: greedy
        currentMax = -1
        n = len(arr)
        for i in range(n - 1, -1, -1):
            oldValue = arr[i]
            arr[i] = currentMax
            currentMax = max(currentMax, oldValue)
        return arr