class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        # time: O(N)
        # space: O(1)
        # method: prefix, suffix sum
        n = len(arr)
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        index1, index2 = -1, -1
        prefix, suffix = 0, 0
        for i in range(n):
            prefix += arr[i]
            if prefix == target:
                index1 = i
                break

        if index1 == -1:
            return False

        for i in range(n - 1, -1, -1):
            suffix += arr[i]
            if suffix == target:
                index2 = i
                break
        
        if index2 == -1:
            return False

        return index1 + 1 < index2